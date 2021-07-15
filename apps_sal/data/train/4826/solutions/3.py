import re

LEGS = r'[a-z]'
BODY = r'[|};&#\[\]/><()*]'

counRobots = lambda a,type: str(sum( len(re.findall(LEGS + BODY + "{2}0" + BODY + "{2}0" + BODY + "{2}" + LEGS,s.lower())) for s in a if type in s.lower() ))
count_robots = lambda a : [ counRobots(a,"automatik") + " robots functioning automatik",  counRobots(a,"mechanik") + " robots dancing mechanik"]
