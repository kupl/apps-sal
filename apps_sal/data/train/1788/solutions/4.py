from operator import xor
from functools import reduce


def choose_move(game_state):
    """Chooses a move to play given a game state"""
    nim_sum = reduce(xor, game_state)
    to_take = (s - (s ^ nim_sum) for s in game_state)
    return next((i, t) for i, t in enumerate(to_take) if t > 0)
