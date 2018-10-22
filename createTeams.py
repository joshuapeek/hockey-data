from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Team, Base, Player, User

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


# Teams for Atlantic Division
toronto = Team(city="Toronto",
               name="Maple Leafs",
               conference="Eastern",
               division="Atlantic",
               user_id="1")
session.add(toronto)
session.commit()

montreal = Team(city="Montreal",
                name="Canadiens",
                conference="Eastern",
                division="Atlantic",
                user_id="1")
session.add(montreal)
session.commit()

ottawa = Team(city="Ottawa",
              name="Senators",
              conference="Eastern",
              division="Atlantic",
              user_id="1")
session.add(ottawa)
session.commit()

tampaBay = Team(city="Tampa Bay",
                name="Lightning",
                conference="Eastern",
                division="Atlantic",
                user_id="1")
session.add(tampaBay)
session.commit()

buffalo = Team(city="Buffalo",
               name="Sabres",
               conference="Eastern",
               division="Atlantic",
               user_id="1")
session.add(buffalo)
session.commit()

boston = Team(city="Boston",
              name="Bruins",
              conference="Eastern",
              division="Atlantic",
              user_id="1")
session.add(boston)
session.commit()

florida = Team(city="Florida",
               name="Panthers",
               conference="Eastern",
               division="Atlantic",
               user_id="1")
session.add(florida)
session.commit()

detroit = Team(city="Detroit",
               name="Red Wings",
               conference="Eastern",
               division="Atlantic",
               user_id="1")
session.add(detroit)
session.commit()


user1 = User(username="Unknown",
             email="nope@nope.com",
             picture="picture")
session.add(user1)
session.commit()


player1 = Player(firstName="Dylan", lastName="Larkin", position="C",
                 team=detroit, height="""6' 1" """, weight="198 lb",
                 birthdate="July 30, 1996", birthCity="Waterford",
                 birthLocation="Michigan", birthNation="USA", user_id="1",
                 bio=""" The moment was duly noted and set down for
                 posterity by all those
    who hold the Detroit Red Wings near and dear to their heart.
     Only 20 seconds into the second period of Larkin's NHL debut, Oct. 9,
     2015, the phenom from Waterford, Mich., took a pass from Henrik
     Zetterberg and snapped a laser of a shot top-shelf past
     Toronto Maple Leafs goaltender Jonathan Bernier. Larkin also
     added an assist in the 4-0 victory.
     The 19-year-old Larkin, selected in the first round (No. 15) of the
     2014 NHL Draft, became the first teenager to start a season on the
     Red Wings roster since Jiri Fischer in 1999. Then again, so much about
     Larkin's rise has been meteoric.
     He made the leap to the NHL after one season at the University of
     Michigan, where his 47 points led Big Ten rookies and placed him second
     in the nation among freshmen. Foregoing his final three years of college
     eligibility and signing a three-year entry-level contract, Larkin began
     his pro career with Grand Rapids just in time for the American Hockey
     League playoffs, where he scored three goals and five points in six games.
     In 2015-16, Larkin became the sixth rookie in Red Wings history to lead
     the team in goals (23), the first since Dale McCourt in 1979-80.
     He also had a plus-11 rating, scored five game-winning goals and
     took 221 shots on goal.
     Larkin became the first teenager since former Red Wing Steve
     Yzerman in 1984-85 to score goals in four consecutive games
     (Nov. 16-21), and he finished the month with seven goals
     and 10 points in 13 games and was named NHL Rookie of the Month.
     Invited to play at the NHL All-Star Game, Larkin participated in the
     Fastest Skater competition during All-Star Weekend and had a time of
     13.172 seconds, breaking Mike Gartner's record of 13.386.
     Gartner set the record in 1996, six months before Larkin was born. """)

session.add(player1)
session.commit()


player2 = Player(firstName="Auston", lastName="Matthews", position="C",
                 team=toronto, height="""6' 3" """, weight="220 lb",
                 birthdate="September 17, 1997", birthCity="San Ramon",
                 birthLocation="California", birthNation="USA", user_id="1",
                 bio=""""Matthews is the NHL's Sun Belt growth come to
                 spectacular life.
    Who would have thought a decade or so ago that a player raised in
    Scottsdale, Arizona, would be the No. 1 pick in the 2016 NHL Draft --
    and a potential franchise player for the Toronto Maple Leafs?
     Matthews was the first United States-born player to be chosen
     No. 1 since the Chicago Blackhawks took Patrick Kane with the first
     pick in the 2007 NHL Draft. While growing up, he idolized players such
     Shane Doan and Daniel Briere, members of the Phoenix/Arizona Coyotes,
     a franchise that relocated in 1996 from Winnipeg. Matthews was an
     all-around athlete who chose to focus on hockey as an adolescent, and
     he excelled at every level of the game on his unique path to the NHL.
     With USA Hockey's National Team Development Program in 2014-15,
     Matthews set United States Under-18 team records for a single
     season with 55 goals and 117 points (surpassing Kane's 52 goals
     and 102 points in 2005-06). The performance was a springboard not
     to major junior or college hockey, but to a one-and-done NHL
     prep season in Switzerland.
     Playing in National League A, the top Swiss pro league, the
     18-year-old center had 24 goals (fourth in the league) and
     46 points (10th) in 36 games with Zurich in 2015-16.
     He played for the United States at the 2016 IIHF Junior World
     Championship, where he tied for the tournament lead with seven
     goals and helped the U.S. win a bronze medal, and at the
     IIHF 2016 World Championship, where he led the U.S. with six
     goals and tied for the lead in points with nine.
     Marc Crawford, Matthews' coach with Zurich and a 15-year veteran
     behind NHL benches, likened him to Joe Sakic, the Hockey Hall of
     Fame center for the Colorado Avalanche. Crawford said Matthews,
     who possesses a deadly wrist shot, might be the best puck-handling
     center he has seen.
     Matthews had a record-setting NHL debut on Oct. 13, 2016, when he
     scored four goals, becoming the first player in the League's modern
     era to do so. He led all rookies in goals (40), points (69) and shots
     on goal (279) in 2016-17 to win the Calder Trophy, awarded to the
     NHL's rookie of the year. He also helped the Maple Leafs advance
     to the Stanley Cup Playoffs for the second time since 2004.
     Injuries limited Matthews to 62 games in 2017-18, but he finished
     with 63 points (34 goals, 29 assists) and helped the Maple Leafs
     return to the playoffs.""")

session.add(player2)
session.commit()


player3 = Player(firstName="Mark", lastName="Pysyk", position="D", user_id="1",
                 team=florida, height="""6' 1" """, weight="200 lb",
                 birthdate="January 11, 1992", birthCity="Sherwood Park",
                 birthLocation="AB", birthNation="CAN", bio="""Pysyk doesn't
    consider himself a superstitious sort, but you wouldn't know it from
    watching his pregame ritual. He always dresses left-to-right: starting
    with the left skate, left glove, left shin pad, etc.
     And if he plays a good game or his team wins, he'll make a point of
     wearing the same suit-and-tie combination for the next game.""")

session.add(player3)
session.commit()


player4 = Player(firstName="Tomas", lastName="Tatar", position="LW",
                 team=montreal, height="""5' 10" """, weight="185 lb",
                 birthdate="December 1, 1990", birthCity="Ilava", user_id="1",
                 birthLocation="", birthNation="SVK", bio="""Tatar appeared on
    track for a fourth straight 20-goal season with the Detroit Red Wings
    in 2017-18 when he was traded to the Vegas Golden Knights for three
    draft picks on Feb. 26, 2018.
     The trade gave Vegas a player who had averaged more than 23 goals
     during his first four full seasons with the Red Wings.""")

session.add(player4)
session.commit()


player5 = Player(firstName="Thomas", lastName="Chabot", position="D",
                 team=ottawa, height="""6' 2" """, weight="196 lb", user_id="1",
                 birthdate="January 30, 1997", birthCity="Sainte-Marie",
                 birthLocation="QC", birthNation="CAN", bio="""Chabot, a
    defenseman taken by the Ottawa Senators in the first round (No. 18)
    of the 2015 NHL Draft, had a solid rookie season in 2017-18,
    finishing with 25 points (nine goals, 16 assists) in 63 games.
     Chabot made the Senators out of training camp in 2016-17. But
     after playing in one game, against the Arizona Coyotes on
     Oct. 18, 2016, he was returned to Saint John of the Quebec Major
     Junior Hockey League.""")

session.add(player5)
session.commit()


player6 = Player(firstName="Nikita", lastName="Kucherov", position="RW",
                 team=tampaBay, height="""5' 11" """, weight="178 lb",
                 birthdate="June 17, 1993", birthCity="Maykop", user_id="1",
                 birthLocation="", birthNation="RUS", bio="""Kucherov was a
    second-round pick (No. 58) by the Tampa Bay Lightning in the 2011
    NHL Draft, but he has played like a first-round talentselfself.
     The 5-foot-11, 178-pound forward from Moscow spent the 2011-12
     season in Russia, then came to North America and played in the
     Quebec Major Junior Hockey League in 2012-13.""")

session.add(player6)
session.commit()


player7 = Player(firstName="Jack", lastName="Eichel", position="C", user_id="1",
                 team=buffalo, height="""6' 2" """, weight="200 lb",
                 birthdate="October 28, 1996", birthCity="North Chelmsford",
                 birthLocation="MA", birthNation="USA", bio="""The No. 2
    pick in the 2015 NHL Draft, Eichel entered the League having
    experienced plenty of success at a young age.
     On April 10, 2015, he became the second freshman to win the
     Hobey Baker Award as the top college player, joining Paul Kariya
     (1993). Playing 40 games for the Boston University, Eichel had 26
     goals and 71 points to lead the nation in scoring.""")

session.add(player7)
session.commit()


player8 = Player(firstName="David", lastName="Pastrnak", position="RW",
                 team=boston, height="""6' 0" """, weight="188 lb",
                 birthdate="May 25, 1996", birthCity="Havirov", user_id="1",
                 birthLocation="", birthNation="CZE", bio="""When Pastrnak
                 walked
    on stage at the Wells Fargo Center in Philadelphia as the No. 25
    player chosen in the 2014 NHL Draft by the Boston Bruins, he
    kissed his hand and pointed to the heavens.
     The tribute, personal and heartfelt, was for his father, an
     adviser, cheerleader, inspiration and hockey/life coach,
     who had died of cancer 13 months earlier. Milan Pastrnak had always
     dreamed of his son playing in the NHL, and now here was David
     slipping the famed Bruins jersey over his head.""")

session.add(player8)
session.commit()

# Secondary Players /////////////
player9 = Player(firstName="Secondary", lastName="Player", position="G",
                 team=toronto, height="""5' 10" """, weight="175 lb",
                 birthdate="July 16, 1986", birthCity="Lansing", user_id="1",
                 birthLocation="Michigan", birthNation="USA",
                 bio="""Didn't start playing ice hockey until adulthood,
    and really... has no place in the NHL.""")

session.add(player9)
session.commit()


player10 = Player(firstName="Secondary", lastName="Player", position="G",
                  team=montreal, height="""5' 10" """, weight="175 lb",
                  birthdate="July 16, 1986", birthCity="Lansing", user_id="1",
                  birthLocation="Michigan", birthNation="USA", bio="""Didn't
                  start
    playing ice hockey until adulthood, and really...
    has no place in the NHL.""")

session.add(player10)
session.commit()


player11 = Player(firstName="Secondary", lastName="Player", position="G",
                  team=ottawa, height="""5' 10" """, weight="175 lb",
                  birthdate="July 16, 1986", birthCity="Lansing",
                  birthLocation="Michigan", birthNation="USA", user_id="1",
                  bio="""Didn't start playing ice hockey until adulthood,
    and really... has no place in the NHL.""")

session.add(player11)
session.commit()


player12 = Player(firstName="Secondary", lastName="Player", position="G",
                  team=tampaBay, height="""5' 10" """, weight="175 lb",
                  birthdate="July 16, 1986", birthCity="Lansing",
                  birthLocation="Michigan", birthNation="USA", user_id="1",
                  bio="""Didn't start playing ice hockey until adulthood,
                  and really...
    has no place in the NHL.""")

session.add(player12)
session.commit()


player13 = Player(firstName="Secondary", lastName="Player", position="G",
                  team=buffalo, height="""5' 10" """, weight="175 lb",
                  birthdate="July 16, 1986", birthCity="Lansing",
                  birthLocation="Michigan", birthNation="USA", user_id="1",
                  bio="""Didn't start playing ice hockey until adulthood,
                  and really...
    has no place in the NHL.""")

session.add(player13)
session.commit()


player14 = Player(firstName="Secondary", lastName="Player", position="G",
                  team=boston, height="""5' 10" """, weight="175 lb",
                  birthdate="July 16, 1986", birthCity="Lansing",
                  birthLocation="Michigan", birthNation="USA", user_id="1",
                  bio="""Didn't start playing ice hockey until adulthood,
                  and really...
    has no place in the NHL.""")

session.add(player14)
session.commit()


player15 = Player(firstName="Secondary", lastName="Player", position="G",
                  team=florida, height="""5' 10" """, weight="175 lb",
                  birthdate="July 16, 1986", birthCity="Lansing",
                  birthLocation="Michigan", birthNation="USA", user_id="1",
                  bio="""Didn't start playing ice hockey until adulthood, and
                  really... has no place in the NHL.""")

session.add(player15)
session.commit()


player16 = Player(firstName="Secondary", lastName="Player", position="G",
                  team=detroit, height="""5' 10" """, weight="175 lb",
                  birthdate="July 16, 1986", birthCity="Lansing",
                  birthLocation="Michigan", birthNation="USA", user_id="1",
                  bio="""Didn't start playing ice hockey until adulthood, and
                  really... has no place in the NHL.""")

session.add(player16)
session.commit()

print "Added Teams and Players!"
