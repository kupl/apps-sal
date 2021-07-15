from operator import xor
from itertools import imap

def choose_move(game_state):
    ns = reduce(xor, game_state)
    for i, p, s in imap(lambda (k, v): (k, v, ns ^ v), enumerate(game_state)):
        if s < p: return (i, p - s)
