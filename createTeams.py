from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Team, Base, Player

engine = create_engine('sqlite:///hockey.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


#Teams for Atlantic Division
toronto = Team(city = "Toronto", name = "Maple Leafs", conference = "Eastern", division = "Atlantic")
session.add(toronto)
session.commit()

montreal = Team(city = "Montreal", name = "Canadiens", conference = "Eastern", division = "Atlantic")
session.add(montreal)
session.commit()

ottawa = Team(city = "Ottawa", name = "Senators", conference = "Eastern", division = "Atlantic")
session.add(ottawa)
session.commit()

tampaBay = Team(city = "Tampa Bay", name = "Lightning", conference = "Eastern", division = "Atlantic")
session.add(tampaBay)
session.commit()

buffalo = Team(city = "Buffalo", name = "Sabres", conference = "Eastern", division = "Atlantic")
session.add(buffalo)
session.commit()

boston = Team(city = "Boston", name = "Bruins", conference = "Eastern", division = "Atlantic")
session.add(boston)
session.commit()

florida = Team(city = "Florida", name = "Panthers", conference = "Eastern", division = "Atlantic")
session.add(florida)
session.commit()

detroit = Team(city = "Detroit", name = "Red Wings", conference = "Eastern", division = "Atlantic")
session.add(detroit)
session.commit()


#Players for Detroit Red Wings
player1 = Player(firstName = "Dylan", lastName = "Larkin", position = "C",
    team = detroit, height = """6' 1" """, weight = "198 lb", birthdate = "July 30, 1996", birthCity = "Waterford",
    birthLocation = "Michigan", birthNation = "USA", bio = """ The moment was duly noted and set down for posterity by all those who hold the Detroit Red Wings near and dear to their heart.
Only 20 seconds into the second period of Larkin's NHL debut, Oct. 9, 2015, the phenom from Waterford, Mich., took a pass from Henrik Zetterberg and snapped a laser of a shot top-shelf past Toronto Maple Leafs goaltender Jonathan Bernier. Larkin also added an assist in the 4-0 victory.
The 19-year-old Larkin, selected in the first round (No. 15) of the 2014 NHL Draft, became the first teenager to start a season on the Red Wings roster since Jiri Fischer in 1999. Then again, so much about Larkin's rise has been meteoric.
He made the leap to the NHL after one season at the University of Michigan, where his 47 points led Big Ten rookies and placed him second in the nation among freshmen. Foregoing his final three years of college eligibility and signing a three-year entry-level contract, Larkin began his pro career with Grand Rapids just in time for the American Hockey League playoffs, where he scored three goals and five points in six games.
In 2015-16, Larkin became the sixth rookie in Red Wings history to lead the team in goals (23), the first since Dale McCourt in 1979-80. He also had a plus-11 rating, scored five game-winning goals and took 221 shots on goal.
Larkin became the first teenager since former Red Wing Steve Yzerman in 1984-85 to score goals in four consecutive games (Nov. 16-21), and he finished the month with seven goals and 10 points in 13 games and was named NHL Rookie of the Month.
Invited to play at the NHL All-Star Game, Larkin participated in the Fastest Skater competition during All-Star Weekend and had a time of 13.172 seconds, breaking Mike Gartner's record of 13.386. Gartner set the record in 1996, six months before Larkin was born. """)

session.add(player1)
session.commit()


player2 = Player(firstName = "Auston", lastName = "Matthews", position = "C",
    team = toronto, height = """6' 3" """, weight = "220 lb", birthdate = "September 17, 1997", birthCity = "San Ramon",
    birthLocation = "California", birthNation = "USA", bio = """"Matthews is the NHL's Sun Belt growth come to spectacular life. Who would have thought a decade or so ago that a player raised in Scottsdale, Arizona, would be the No. 1 pick in the 2016 NHL Draft -- and a potential franchise player for the Toronto Maple Leafs?

Matthews was the first United States-born player to be chosen No. 1 since the Chicago Blackhawks took Patrick Kane with the first pick in the 2007 NHL Draft. While growing up, he idolized players such Shane Doan and Daniel Briere, members of the Phoenix/Arizona Coyotes, a franchise that relocated in 1996 from Winnipeg. Matthews was an all-around athlete who chose to focus on hockey as an adolescent, and he excelled at every level of the game on his unique path to the NHL.
With USA Hockey's National Team Development Program in 2014-15, Matthews set United States Under-18 team records for a single season with 55 goals and 117 points (surpassing Kane's 52 goals and 102 points in 2005-06). The performance was a springboard not to major junior or college hockey, but to a one-and-done NHL prep season in Switzerland.
Playing in National League A, the top Swiss pro league, the 18-year-old center had 24 goals (fourth in the league) and 46 points (10th) in 36 games with Zurich in 2015-16. He played for the United States at the 2016 IIHF Junior World Championship, where he tied for the tournament lead with seven goals and helped the U.S. win a bronze medal, and at the IIHF 2016 World Championship, where he led the U.S. with six goals and tied for the lead in points with nine.
Marc Crawford, Matthews' coach with Zurich and a 15-year veteran behind NHL benches, likened him to Joe Sakic, the Hockey Hall of Fame center for the Colorado Avalanche. Crawford said Matthews, who possesses a deadly wrist shot, might be the best puck-handling center he has seen.
Matthews had a record-setting NHL debut on Oct. 13, 2016, when he scored four goals, becoming the first player in the League's modern era to do so. He led all rookies in goals (40), points (69) and shots on goal (279) in 2016-17 to win the Calder Trophy, awarded to the NHL's rookie of the year. He also helped the Maple Leafs advance to the Stanley Cup Playoffs for the second time since 2004.
Injuries limited Matthews to 62 games in 2017-18, but he finished with 63 points (34 goals, 29 assists) and helped the Maple Leafs return to the playoffs.""")

session.add(player2)
session.commit()
#
#player3 = Player(firstName = "", lastName = "", position = "",
#    team = "", height = "", weight = "", birthdate = "", birthCity = "",
#    birthLocation = "", birthNation = "", bio = "")
#
#player4 = Player(firstName = "", lastName = "", position = "",
#    team_id = detroit, height = "", weight = "", birthdate = "", birthCity = "",
#    birthLocation = "", birthNation = "", bio = "")
#
#menuItem1 = MenuItem(name = "French Fries", description = "with garlic and parmesan", price = "$2.99", course = "Appetizer", restaurant = restaurant1)
#
#session.add(menuItem1)
#session.commit()



print "Added Teams and Players!"
