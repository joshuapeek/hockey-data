from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Team, Player

app = Flask(__name__)

engine = create_engine('sqlite:///hockey.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


## STANDARD USE //////////////////////////////////////
# These pages are served for standard users

#Main page - displays teams in db
@app.route('/')
def mainPage():
    team = session.query(Team).all()
    output = ''
    for i in team:
        output += i.city
        output += ' '
        output += i.name
        output += '</br>'
    return output

#Team page - displays players in db, from a given team
@app.route('/<int:team_id>/')
def teamPage(team_id):
    team = session.query(Team).filter_by(id = team_id).one()
    player = session.query(Player).filter_by(team_id = team.id)
    output = ''
    for i in player:
        output += 'Name: ' + i.firstName + ' ' + i.lastName + '</br>'
        output += 'Position: ' + i.position + '</br></br>'
    return output

#Player page - displays player info in db, for a given team, player
@app.route('/<int:team_id>/<int:player_id>/')
def playerPage(team_id, player_id):
    team = session.query(Team).filter_by(id = team_id).one()
    player = session.query(Player).filter_by(team_id=team_id, id=player_id).all()
    output = ''
    for i in player:
        output += i.firstName + ' ' + i.lastName + '</br>'
        output += i.team.city + ' ' + i.team.name + ' | ' + i.position + '</br>'
        output += i.height + ' | ' + i.weight
        output += ' | Birthdate: ' + i.birthdate + '</br>'
        output += i.birthCity + ', ' + i.birthLocation
        if i.birthLocation != "":
            output += ', '
        output += i.birthNation + '</br>'
        output += i.bio + '</br></br></br>'
    return output
#    return player.firstName

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
    return "This is the create a team page!"

#New Player page
@app.route('/<int:team_id>/new/', methods=['GET', 'POST'])
def newPlayerPage(team_id):
    return "This is the create a player page!"


## EDIT --------------------------------------------
#Edit Team page
@app.route('/<int:team_id>/edit/', methods=['GET', 'POST'])
def editTeamPage(team_id):
    return "This is the edit a team page."

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
