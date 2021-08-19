from collections import OrderedDict


def common_ground(s1, s2):
    xs = set(s1.split())
    return ' '.join((x for x in OrderedDict.fromkeys(s2.split()) if x in xs)) or 'death'
