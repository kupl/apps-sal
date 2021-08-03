from itertools import groupby
from re import findall

F = {'FIRE': lambda k: 'You' + ' and you' * (k - 1) + ' are fired!',
     'FURY': lambda k: 'I am' + ' really' * (k - 1) + ' furious.'}


def fire_and_fury(tweet):
    r = [F[w](sum(1 for _ in g)) for w, g in groupby(findall('FIRE|FURY', tweet))]

    return ' '.join(r) if r and all(c in 'EFIRUY' for c in tweet)else 'Fake tweet.'
