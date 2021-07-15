from operator import itemgetter

def last(s):
    return sorted(s.split(), key=itemgetter(-1))
