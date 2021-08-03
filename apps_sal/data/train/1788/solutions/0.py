from operator import xor


def choose_move(game_state):
    """Chooses a move to play given a game state"""
    x = reduce(xor, game_state)
    for i, amt in enumerate(game_state):
        if amt ^ x < amt:
            return (i, amt - (amt ^ x))
