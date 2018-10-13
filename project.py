from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Team, Player
from sqlalchemy.pool import StaticPool

app = Flask(__name__)

engine = create_engine('sqlite:///hockey.db',
    connect_args={'check_same_thread':False},
    poolclass=StaticPool)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


## STANDARD USE //////////////////////////////////////
# These pages are served for standard users

#Main page - displays teams in db
@app.route('/')
def mainPage():
    teams = session.query(Team).all()
    return render_template('teams.html', teams=teams)

#Team page - displays players in db, from a given team
@app.route('/<int:team_id>/')
def teamPage(team_id):
    team = session.query(Team).filter_by(id = team_id).one()
    players = session.query(Player).filter_by(team_id = team_id).all()
    return render_template('roster.html', team=team, players=players)

#Player page - displays player info in db, for a given team, player
@app.route('/<int:team_id>/<int:player_id>/')
def playerPage(team_id, player_id):
    team = session.query(Team).filter_by(id = team_id).one()
    player = session.query(Player).filter_by(team_id=team_id, id=player_id).one()
    return render_template('player.html', team=team, player=player)


## API USE //////////////////////////////////////
# These pages are served via API request

#Main page: displays teams in db, serialized in JSON format
@app.route('/JSON')
def mainPageJSON():
    teams = session.query(Team).all()
    return jsonify(Team=[t.serialize for t in teams])

#Team page: displays players from a given team in db, serialized in JSON format
@app.route('/<int:team_id>/JSON')
def teamPageJSON(team_id):
    team = session.query(Team).filter_by(id = team_id).one()
    players = session.query(Player).filter_by(team_id = team_id).all()
    return jsonify(Roster=[i.serialize for i in players])



## ADMIN USE //////////////////////////////////////
# These pages are served for admin users

#Admin Login page
@app.route('/login/')
def adminLogin():
    return "This is the admin login page."

#Admin Control page - displays admin controls for editing teams, players
@app.route('/admin/')
def adminPage():
    return "This is the admin control page."


## NEW --------------------------------------------
#New Team page
@app.route('/new/', methods=['GET', 'POST'])
def newTeamPage():
    if request.method == 'POST':
        newTeam = Team(
        city=request.form['city'],
        name=request.form['name'],
        conference=request.form['conference'],
        division=request.form['division'],
        )
        session.add(newTeam)
        session.commit()
        flash("New Team Created!")
        return redirect(url_for('mainPage'))
    else:
        return render_template('newTeam.html')

#New Player page
@app.route('/<int:team_id>/new/', methods=['GET', 'POST'])
def newPlayerPage(team_id):
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
        return render_template('newPlayer.html',team_id=team_id)


## EDIT --------------------------------------------
#Edit Team page
@app.route('/<int:team_id>/edit/', methods=['GET', 'POST'])
def editTeamPage(team_id):
    editedTeam = session.query(Team).filter_by(id=team_id).one()
    if request.method == 'POST':
        if request.form['city']:
            editedTeam.city=request.form['city']
            editedTeam.name=request.form['name']
            editedTeam.conference=request.form['conference']
            editedTeam.division=request.form['division']
        session.add(editedTeam)
        session.commit()
        flash("Team Edited!")
        return redirect(url_for('mainPage'))
    else:
        return render_template('editTeam.html', i=editedTeam)

#Edit Player page
@app.route('/<int:team_id>/<int:player_id>/edit/', methods=['GET', 'POST'])
def editPlayerPage(team_id, player_id):
    editedPlayer = session.query(
    Player).filter_by(team_id=team_id, id=player_id).one()
    if request.method == 'POST':
        if request.form['firstName']:
            editedPlayer.firstName=request.form['firstName']
            editedPlayer.lastName=request.form['lastName']
            editedPlayer.position=request.form['position']
            editedPlayer.height=request.form['height']
            editedPlayer.weight=request.form['weight']
            editedPlayer.birthdate=request.form['birthdate']
            editedPlayer.birthCity=request.form['birthCity']
            editedPlayer.birthLocation=request.form['birthLocation']
            editedPlayer.birthNation=request.form['birthNation']
            editedPlayer.bio=request.form['bio']
        session.add(editedPlayer)
        session.commit()
        flash("Player Edited!")
        return redirect(url_for('playerPage', team_id = team_id, player_id=editedPlayer.id))
    else:
        return render_template('editPlayer.html', i=editedPlayer, team_id=team_id)


## DELETE --------------------------------------------
#Delete Team page
@app.route('/<int:team_id>/delete/', methods=['GET', 'POST', 'DELETE'])
def deleteTeamPage(team_id):
    teamToDelete = session.query(
    Team).filter_by(id=team_id).one()
    if request.method == 'POST':
        session.delete(teamToDelete)
        session.commit()
        flash("Team Removed!")
        return redirect(url_for('mainPage'))
    else:
        return render_template('deleteTeam.html', i=teamToDelete)

#Delete Player page
@app.route('/<int:team_id>/<int:player_id>/delete/', methods=['GET', 'POST', 'DELETE'])
def deletePlayerPage(team_id, player_id):
    playerToDelete = session.query(
    Player).filter_by(team_id=team_id, id=player_id).one()
    if request.method == 'POST':
        session.delete(playerToDelete)
        session.commit()
        flash("Player Removed!")
        return redirect(url_for('teamPage', team_id=team_id))
    else:
        return render_template('deletePlayer.html', i=playerToDelete)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
