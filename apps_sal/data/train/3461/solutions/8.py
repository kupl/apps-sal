from collections import OrderedDict


def common_ground(s1, s2):
    s = ' '.join((w for w in OrderedDict.fromkeys(s2.split()) if w in s1.split()))
    return s if s else 'death'
