from flask import Flask, render_template, request, redirect, url_for
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
    players = session.query(Player).filter_by(team_id = team.id).all()
    return render_template('roster.html', team=team, players=players)

#Player page - displays player info in db, for a given team, player
@app.route('/<int:team_id>/<int:player_id>/')
def playerPage(team_id, player_id):
    team = session.query(Team).filter_by(id = team_id).one()
    player = session.query(Player).filter_by(team_id=team_id, id=player_id).one()
    return render_template('player.html', team=team, player=player)

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
        return redirect(url_for('mainPage'))
    else:
        return render_template('newTeam.html')

#New Player page
@app.route('/<int:team_id>/new/', methods=['GET', 'POST'])
def newPlayerPage(team_id):
    if request.method == 'POST':
        newPlayer = Player(
        firstName=request.form['firstName'],
        lastName=request.form['lastName'],
        position=request.form['position'],
        height=request.form['height'],
        weight=request.form['weight'],
        birthdate=request.form['birthdate'],
        birthCity=request.form['birthCity'],
        birthLocation=request.form['birthLocation'],
        birthNation=request.form['birthNation'],
        bio=request.form['bio'],
        team_id=team_id
        )
        session.add(newPlayer)
        session.commit()
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
        if request.form['conference'] != "":
            editedTeam.conference=request.form['conference']
        if request.form['division'] != "":
            editedTeam.division=request.form['division']
        session.add(editedTeam)
        session.commit()
        return redirect(url_for('mainPage'))
    else:
        return render_template('editTeam.html', i=editedTeam)

#Edit Player page
@app.route('/<int:team_id>/<int:player_id>/edit/', methods=['GET', 'POST'])
def editPlayerPage(team_id, player_id):
    return "This is the edit a player page."


## DELETE --------------------------------------------
#Delete Team page
@app.route('/<int:team_id>/delete/', methods=['GET', 'POST', 'DELETE'])
def deleteTeamPage(team_id):
    return "This is the delete a team page."

#Delete Player page
@app.route('/<int:team_id>/<int:player_id>/delete/', methods=['GET', 'POST', 'DELETE'])
def deletePlayerPage(team_id, player_id):
    return "This is the delete a player page."


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
