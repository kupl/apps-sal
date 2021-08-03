from itertools import chain


def crap(garden, bags, cap):
    return (lambda x: 'Dog!!' if x.count('D') else 'Clean' if x.count('@') <= bags * cap else 'Cr@p')(list(chain(*garden)))
