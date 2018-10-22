# hockey-database
This project consists of a database, server-side code, and webpages.
Web-based access is given to create, read, update and delete data about hockey teams and players within a database. Data can also be read in JSON format.

hockey-database demonstrates mastery of skills learned within the second project of Udacity's Full Stack Web Developer Nanodegree.

hockey-database was written by Joshua Peek.




## Index
1. [Download and Installation: General](#download-and-installation)
2. [Download and Installation: Virtual Machine Elements](#virtual-machine-elements)
3. [Download and Installation: Python3 and Dependencies](#python3-and-dependencies)
4. [Download and Installation: hockey-database files](#hockey-database-itself)
5. [Project Requirements](#project-requirements)
6. ['hockey-database' Table Structures](#hockey-database-table-structures)
7. [Code Design](#code-design)
8. [Code Design: project.py](#project.py-file)
8. [Code Design: database_setup.py](#database-setup.py-file)
8. [Code Design: createTeams.py](#createteams.py-file)
8. [Thanks & Acknowledgement](#thanks--acknowledgement)




## Download and Installation
Be sure to follow these items in order, starting at the top, and working downward.
Ex: _Virtual Machine Elements_ first, and _The 'news' Database_ last.


#### Virtual Machine Elements

This project makes use of a Linux-based virtual machine (VM).
It's suggested that you use the tools Vagrant and VirtualBox to install and manage the VM.
The course provides [this helpful video](https://www.youtube.com/watch?v=djnqoEO2rLc) as a conceptual overview of virtual machines and Vagrant, if you're not familiar with either.

###### VirtualBox installation:
1. [Download VirtualBox from VirtualBox.org, here.](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
2. Install the _platform package_ for your operating system. You will not need the extension pack or SDK.

###### Vagrant installation:
1. [Download Vagrant from VagrantUp.com, here](https://www.vagrantup.com/downloads.html)
2. Install the appropriate version for your operating system.
3. Windows users: If prompted, be sure to grant network permissions to Vagrant, or make a firewall exception.

_Run `vagrant --version` in your terminal. A returned version number verifies correct installation._

###### VM Configuration:
1. Within GitHub, fork and clone [the configuration repository, here](https://github.com/udacity/fullstack-nanodegree-vm)
2. When launching Vagrant, be sure to `cd` into the **vagrant** directory created by this Configuration

###### Starting the VM:
1. From your terminal, inside the **vagrant** subdiractory, run the command `vagrant up`.
2. Vagrant will perform necessary setup, which may take several minutes.
3. When setup is completed, use your returned shell prompt to run `vagrant ssh`.
4. Vagrant will log you into your newly installed Linux VM!

_A shell prompt beginning with `vagrant` signifies correct installation._
_Remember to `cd` into the **vagrant** directory!_

[Back to Index](#index)


#### Python3 and Dependencies

The project-logs script makes use of Python3.
To install Python3: [Select the version appropriate for your operating system, here.](https://www.python.org/downloads/)

_Note: If you're using Python2, hockey-database will not work._

You'll also need to install the following libraries for use with Python. For each library, the name and terminal pip install command is given.

###### psycopg2
- Terminal install: `pip install psycopg2`
- [Documentation found here.](https://pypi.org/project/psycopg2/)

###### oauth2client
- Terminal install: `pip install --upgrade oauth2client`

###### Flask
- Terminal install: `pip install Flask`
- [Documentation found here.](http://flask.pocoo.org/docs/1.0/)

###### SQLAlchemy
- Terminal install `pip install SQLAlchemy`
- [Documentation found here.](https://www.sqlalchemy.org/)

###### Requests
- [For help installing Requests, visit this page.](http://docs.python-requests.org/en/master/user/install/#install)
- [Documentation found here.](http://docs.python-requests.org/en/master/)

[Back to Index](#index)

#### hockey-database itself

PostgreSQL is already installed on your VM, as part of the VM Configuration, detailed above.
To use the 'news' database, you'll need to have the provided PostgreSQL database 'news' installed.
1. [Download the 'news' database here.](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
2. Unzip the file, and locate the contained file called `newsdata.sql`
3. Place this `newsdata.sql` file into the `vagrant` directory.
4. Before loading the data, be sure your VM is on the `vagrant` directory. If not, `cd` into it.
5. Load the data by using the command `psql -d news -f newsdata.sql`
   - This command connects to a 'news' database, and runs a series of SQL statements, setting up the 'news' database for use.


###### Launching hockey-database
To launch the script:
1. Enter the following within the VM terminal: `python project.py`
2. You should see a message letting you know that the server is now running.
3. Next, open a browser and visit [http://localhost:5000/](http://localhost:5000/)
4. You should see the main webpage appear, allowing you to view all teams.

_NOTE: If you're signed in using Google accounts, you should be able to add, edit, and delete both players and teams in the database._

[Back to Index](#index)




## Project Requirements
For those enrolled, [have a look at the full project rubric here.](https://review.udacity.com/#!/rubrics/5/view)

The project's code requirements:
- Conforms to PEP8 style guide for Python code
- Comments are present and effectively explain longer code procedures.
- `README` file includes details of all the steps required to successfully run the application.

The project must meet the following requirements:
- The project implements a JSON endpoint that serves the same information as displayed in the HTML endpoints for an arbitrary item in the catalog.
- Website reads category and item information from a database.
- Website includes a form allowing users to add new items and correctly processes submitted forms.
- Website does include a form to edit/update a current record in the database table and correctly processes submitted forms.
- Website does include a function to delete a current record.
- Create, delete and update operations do consider authorization status prior to execution.
- Page implements a third-party authentication & authorization service (like `Google Accounts` or `Mozilla Persona`) instead of implementing its own authentication & authorization spec.
- Make sure there is a 'Login' and 'Logout' button/link in the project. The aesthetics of this button/link is up to the discretion of the student.

[Back to Index](#index)




## 'hockey-database' Table Structures
There are two tables in the project's database: "team" and "players". Their structures are described below.

_team table:_

|Column|Key?   |Type       |
|------|-------|-----------|
|id|primary|integer    |
|city||text|
|name||text|
|conference ||text|
|division||text|

_players table:_

|Column|Key?   |Type       |
|------|-------|-----------|
|id|Primary|integer|
|firstName||text|
|lastName||text|
|position||text|
|team_id||text|
|team||text|
|height||text|
|weight||text|
|birthdate||text|
|birthCity||text|
|birthLocation||text|
|bio||text|

[Back to Index](#index)




## Code Design

#### project.py file
This project is largely controlled by the project.py file.
Project.py consists of five main sections:
1. [Variable Declarations](#variable-declarations)
2. [Standard Use](#standard-use)
3. [API/JSON Use](#api-json-use)
4. [Authentication](#authentication)
5. [Admin Use](#admin-use)

###### Variable Declarations
- Variables relating to oauth2 usage are defined here
- A variable enabling shorter database query calls is defined



###### Standard Use
- Code defining URI for and pulling required data for the site's home page. Retrieved data is presented via Flask template.
- Code defining URI for and pulling required data for a team-specific roster page. Retrieved data is presented via Flask template.
- Code defining URI for and pulling required data for the team-and-player-specific bio page. Retrieved data is presented via Flask template.



###### API/JSON Use
- Code defining an endpoint URI for API usage, returning same data from "Teams" page in serialized JSON format.
- Code defining an endpoint URI for API usage, returning same data from "Team Roster" page in serialized JSON format.
- Code defining an endpoint URI for API usage, returning same data from "Player Bio" page in serialized JSON format.



###### Authentication
- Code defining URI for a login page, using Google 3rd party authentication
- Code defining URI for a sign-out page



###### Admin Use
- Code defining a URI for "New Team" creation. Points user to a form, then collects form data and uses to create a new team in the database.
- Code defining a URI for "New Player" creation. Points user to a form, then collects form data and uses to create a new player in the database.
- Code defining a URI for "Edit Team" page. Points user to a form, then collects form data and uses to edit an existing team in the database.
- Code defining a URI for "Edit Player" page. Points user to a form, then collects form data and uses to edit an existing player in the database.
- Code defining a URI for "Delete Team" page. Points user to a form to confirm intent, then removes the team from the database.
- Code defining a URI for "Delete Player" page. Points user to a form to confirm intent, then removes the player from the database.



#### database_setup.py file
- Two classes defined: 'team' and 'player'
- Each class defines a table, and specifies fields for that table
- For each class, a function is provided, allowing data to be retrieved in serialized format for API/JSON endpoints



#### createTeams.py file
- This optional file will pre-populate your database with some teams and players, which an authenticated user may then further edit.
- If desired, you may run this file via terminal to pre-populate your database with teams and players.
1. To run this file, first ensure that the `project.py` file is not currently running.
2. Enter the following within the VM terminal: `python createTeams.py`
3. You should see this message in the terminal: `Added Teams and Players!`

[Back to Index](#index)


## Thanks & Acknowledgement
Special thanks to the Udacity Mentors, who've helped tremendously.

[Back to Index](#index)
