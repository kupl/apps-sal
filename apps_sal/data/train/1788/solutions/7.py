from operator import xor
from itertools import imap
from functools import reduce


def choose_move(game_state):
    ns = reduce(xor, game_state)
    for i, p, s in imap(lambda k_v: (k_v[0], k_v[1], ns ^ k_v[1]), enumerate(game_state)):
        if s < p:
            return (i, p - s)
