from operator import itemgetter


def make_string(s):
    return ''.join(map(itemgetter(0), s.split()))
