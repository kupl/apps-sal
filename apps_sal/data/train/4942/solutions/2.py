from collections import Counter


def directions(goal):
    c = Counter(goal)
    (c['N'], c['W']) = (c['N'] - c['S'], c['W'] - c['E'])
    (c['S'], c['E']) = (-c['N'], -c['W'])
    return sorted(c.elements(), key='NSEW'.index)
