import operator


def choose_move(heaps):
    """Chooses a move to play given a game state."""
    x = reduce(operator.xor, heaps)
    return next((i, h - (x ^ h)) for i, h in enumerate(heaps) if (x ^ h) < h)
