import re
LEGS = '[a-z]'
BODY = '[|};&#\\[\\]/><()*]'


def counRobots(a, type):
    return str(sum((len(re.findall(LEGS + BODY + '{2}0' + BODY + '{2}0' + BODY + '{2}' + LEGS, s.lower())) for s in a if type in s.lower())))


def count_robots(a):
    return [counRobots(a, 'automatik') + ' robots functioning automatik', counRobots(a, 'mechanik') + ' robots dancing mechanik']
