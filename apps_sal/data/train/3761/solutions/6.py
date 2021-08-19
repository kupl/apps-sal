from itertools import groupby


def strange_coach(players):
    return ''.join((key for (key, group) in groupby(sorted(players), lambda x: x[0]) if len(list(group)) >= 5)) or 'forfeit'
