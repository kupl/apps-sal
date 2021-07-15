from operator import xor
from functools import reduce

def choose_move(game_state):
    """Chooses a move to play given a game state"""
    diffs = [amount ^ reduce(xor, game_state) for amount in game_state]
    offsets = [pile - diff for pile, diff in zip(game_state, diffs)]
    amount_of_straws = max(offsets)
    return (offsets.index(amount_of_straws), amount_of_straws)

