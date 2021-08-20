from re import findall
from itertools import groupby


def fire_and_fury(tweet):
    m = findall('FIRE|FURY', tweet)
    if set('EFIRUY') < set(tweet):
        m = []
    s = []
    for (x, c) in groupby(m):
        l = len(list(c))
        if x == 'FURY':
            s += ['I am ' + 'really ' * (l - 1) + 'furious.']
        if x == 'FIRE':
            s += ['You ' + 'and you ' * (l - 1) + 'are fired!']
    r = ' '.join(s)
    return r or 'Fake tweet.'
