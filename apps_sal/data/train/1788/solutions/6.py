def choose_move(game_state):
    """Chooses a move to play given a game state"""
    value = reduce(lambda x, y: x ^ y, game_state)
    (i, v) = [(i, v) for (i, v) in enumerate(game_state) if v ^ value < v][0]
    return (i, v - (v ^ value))
