from flask import Flask, render_template, request, redirect
from flask import url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Team, Player
from sqlalchemy.pool import StaticPool
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

# Read client secrets, set as variables for use in authentication
CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
CLIENT_SECRET = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_secret']
redirect_uris = json.loads(
    open('client_secrets.json', 'r').read())['web']['redirect_uris']

app = Flask(__name__)

# set shorthand variable for connecting to database
engine = create_engine('sqlite:///hockey.db',
                       connect_args={'check_same_thread': False},
                       poolclass=StaticPool)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# STANDARD USE //////////////////////////////////////
# These pages are served for standard users


# Main page - displays teams in db
@app.route('/')
def mainPage():
    teams = session.query(Team).all()
    return render_template('teams.html', teams=teams)


# Team page - displays players in db, from a given team
@app.route('/<int:team_id>/')
def teamPage(team_id):
    team = session.query(Team).filter_by(id=team_id).one()
    players = session.query(Player).filter_by(team_id=team_id).all()
    return render_template('roster.html', team=team, players=players)


# Player page - displays player info in db, for a given team, player
@app.route('/<int:team_id>/<int:player_id>/')
def playerPage(team_id, player_id):
    team = session.query(Team).filter_by(id=team_id).one()
    player = session.query(Player).filter_by(
        team_id=team_id, id=player_id).one()
    return render_template('player.html', team=team, player=player)


# API USE //////////////////////////////////////
# These pages are served via API request at JSON endpoint


# JSON Main page: displays teams in db, serialized
@app.route('/JSON')
def mainPageJSON():
    teams = session.query(Team).all()
    return jsonify(Team=[t.serialize for t in teams])


# JSON Team page: displays players from a given team in db, serialized
@app.route('/<int:team_id>/JSON')
def teamPageJSON(team_id):
    team = session.query(Team).filter_by(id=team_id).one()
    players = session.query(Player).filter_by(team_id=team_id).all()
    return jsonify(Roster=[i.serialize for i in players])


# JSON Player page: displays player info in db, serialized
@app.route('/<int:team_id>/<int:player_id>/JSON')
def playerPageJSON(team_id, player_id):
    team = session.query(Team).filter_by(id=team_id).one()
    player = session.query(Player).filter_by(
        team_id=team_id, id=player_id).one()
    return jsonify(Player=player.serialize)


# AUTHENTICATION //////////////////////////////////////
# These pages allow admin users to authenticate and disconnect


# Admin Login page
@app.route('/login/')
def adminLogin():
    # Create CSRF state token
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate CSRF state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')

    # Check if user is already signed in
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps(
            'Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)
    data = answer.json()

    # Store to variable
    login_session['username'] = data['email']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    response = make_response(json.dumps(
        'Signed in Successfully!'), 200)
    response.headers['Content-Type'] = 'application/json'
    return response


# Admin Sign-out: Revokes current user's token, resets login_session
@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user
    access_token = login_session.get('access_token')
    if access_token is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Execute HTTP GET to revoke token
    url = 'https://accounts.google.com/o/oauth2/revoke?'
    url += 'token=%s' % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        # Reset the user's session
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        # Move user back to main page, flash success message
        flash("Disconnected Successfully")
        return redirect('/')
    else:
        # Move user back to main page, flash failure message
        flash("Failed to log out")
        return redirect('/')


# ADMIN USE //////////////////////////////////////
# These pages are served for admin users


# Admin Control page - displays admin controls for editing teams, players
@app.route('/admin/')
def adminPage():
    return "This is the admin control page."


# NEW --------------------------------------------
# New Team page
@app.route('/new/', methods=['GET', 'POST'])
def newTeamPage():
    # Ensure user is signed in
    if 'username' not in login_session:
        return redirect('/login')
    # If GET, serve form; If POST receive data, commit new team to db
    if request.method == 'POST':
        newTeam = Team(
                       city=request.form['city'],
                       name=request.form['name'],
                       conference=request.form['conference'],
                       division=request.form['division'],)
        session.add(newTeam)
        session.commit()
        flash("New Team Created!")
        return redirect(url_for('mainPage'))
    else:
        return render_template('newTeam.html')


# New Player page
@app.route('/<int:team_id>/new/', methods=['GET', 'POST'])
def newPlayerPage(team_id):
    # Ensure user is signed in
    if 'username' not in login_session:
        return redirect('/login')
    # If GET, serve form; If POST receive data, commit new player to db
    if request.method == 'POST':
        newPlayer = Player(firstName=request.form['firstName'],
                           lastName=request.form['lastName'],
                           position=request.form['position'],
                           height=request.form['height'],
                           weight=request.form['weight'],
                           birthdate=request.form['birthdate'],
                           birthCity=request.form['birthCity'],
                           birthLocation=request.form['birthLocation'],
                           birthNation=request.form['birthNation'],
                           bio=request.form['bio'],
                           team_id=team_id)
        session.add(newPlayer)
        session.commit()
        flash("New Player Created!")
        return redirect(url_for('teamPage', team_id=team_id))
    else:
        return render_template('newPlayer.html', team_id=team_id)


# EDIT --------------------------------------------
# Edit Team page
@app.route('/<int:team_id>/edit/', methods=['GET', 'POST'])
def editTeamPage(team_id):
    # Ensure user is signed in
    if 'username' not in login_session:
        return redirect('/login')
    # Pull team specified in URI from db
    editedTeam = session.query(Team).filter_by(id=team_id).one()
    # If GET, serve form; If POST receive data, commit edited team to db
    if request.method == 'POST':
        if request.form['city']:
            editedTeam.city = request.form['city']
            editedTeam.name = request.form['name']
            editedTeam.conference = request.form['conference']
            editedTeam.division = request.form['division']
        session.add(editedTeam)
        session.commit()
        flash("Team Edited!")
        return redirect(url_for('mainPage'))
    else:
        return render_template('editTeam.html', i=editedTeam)


# Edit Player page
@app.route('/<int:team_id>/<int:player_id>/edit/', methods=['GET', 'POST'])
def editPlayerPage(team_id, player_id):
    # Ensure user is signed in
    if 'username' not in login_session:
        return redirect('/login')
    # Pull player specified in URI from db
    editedPlayer = session.query(
        Player).filter_by(team_id=team_id, id=player_id).one()
    # If GET, serve form; If POST receive data, commit edited player to db
    if request.method == 'POST':
        if request.form['firstName']:
            editedPlayer.firstName = request.form['firstName']
            editedPlayer.lastName = request.form['lastName']
            editedPlayer.position = request.form['position']
            editedPlayer.height = request.form['height']
            editedPlayer.weight = request.form['weight']
            editedPlayer.birthdate = request.form['birthdate']
            editedPlayer.birthCity = request.form['birthCity']
            editedPlayer.birthLocation = request.form['birthLocation']
            editedPlayer.birthNation = request.form['birthNation']
            editedPlayer.bio = request.form['bio']
        session.add(editedPlayer)
        session.commit()
        flash("Player Edited!")
        return redirect(url_for(
            'playerPage', team_id=team_id, player_id=editedPlayer.id))
    else:
        return render_template(
            'editPlayer.html', i=editedPlayer, team_id=team_id)


# DELETE --------------------------------------------
# Delete Team page
@app.route('/<int:team_id>/delete/', methods=['GET', 'POST'])
def deleteTeamPage(team_id):
    # Ensure user is signed in
    if 'username' not in login_session:
        return redirect('/login')
    # Pull team specified in URI from db
    teamToDelete = session.query(
        Team).filter_by(id=team_id).one()
    # If GET, serve form; If POST remove team from db
    if request.method == 'POST':
        session.delete(teamToDelete)
        session.commit()
        flash("Team Removed!")
        return redirect(url_for('mainPage'))
    else:
        return render_template('deleteTeam.html', i=teamToDelete)


# Delete Player page
@app.route('/<int:team_id>/<int:player_id>/delete/', methods=['GET', 'POST'])
def deletePlayerPage(team_id, player_id):
    # Ensure user is signed in
    if 'username' not in login_session:
        return redirect('/login')
    # Pull player specified in URI from db
    playerToDelete = session.query(
        Player).filter_by(team_id=team_id, id=player_id).one()
    # If GET, serve form; If POST remove player from db
    if request.method == 'POST':
        session.delete(playerToDelete)
        session.commit()
        flash("Player Removed!")
        return redirect(url_for('teamPage', team_id=team_id))
    else:
        return render_template('deletePlayer.html', i=playerToDelete)


if __name__ == '__main__':
    app.secret_key = CLIENT_SECRET
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
