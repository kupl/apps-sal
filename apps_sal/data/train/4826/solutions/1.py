import re

LEGS = r'[a-z]'
BODY = r'[|};&#\[\]/><()*]'

def counRobots(strng,typeRobot):
    return str(sum( len(re.findall(LEGS + BODY + "{2}0" + BODY + "{2}0" + BODY + "{2}" + LEGS, substr))
                    for substr in map(str.lower, strng)
                    if typeRobot in substr ))

def count_robots(a):
    return ["{} robots functioning automatik".format(counRobots(a, "automatik")),
            "{} robots dancing mechanik".format(counRobots(a, "mechanik"))]



