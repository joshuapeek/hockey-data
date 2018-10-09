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

#Main page
@app.route('/')
def mainPage():
    return "This is the main page!"

#Team page
@app.route('/<int:team_id>/')
def teamPage(team_id):
    return "This is the team page!"

#Player page
@app.route('/<int:team_id>/<int:player_id>/')
def playerPage(team_id, player_id):
    return "This is the player page!"


## ADMIN USE //////////////////////////////////////
# These pages are served for admin users

#Admin Control page
@app.route('/admin/')
def adminPage():
    return "This is the admin control page."


## NEW --------------------------------------------
#New Team page
@app.route('/new/', methods=['GET', 'POST'])
def newTeamPage():
    return "This is the create team page!"

#New Player page
@app.route('/<int:team_id>/new/', methods=['GET', 'POST'])
def newPlayerPage(team_id):
    return "This is the create player page!"


## EDIT --------------------------------------------
#Edit Team page
@app.route('/<int:team_id>/edit/', methods=['GET', 'POST'])
def editTeamPage(team_id):
    return "This is the edit team page."

#Edit Player page
@app.route('/<int:team_id>/<int:player_id>/edit/', methods=['GET', 'POST'])
def editPlayerPage(team_id, player_id):
    return "This is the edit player page."


## DELETE --------------------------------------------
#Delete Team page
@app.route('/<int:team_id>/delete/', methods=['GET', 'POST', 'DELETE'])
def deleteTeamPage(team_id):
    return "This is the delete player page."

#Delete Player page
@app.route('/<int:team_id>/<int:player_id>/delete/', methods=['GET', 'POST', 'DELETE'])
def deletePlayerPage(team_id, player_id):
    return "This is the delete player page."


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
