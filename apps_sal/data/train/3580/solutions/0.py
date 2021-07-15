def get_positions(n):
    return tuple(n // d % 3 for d in (1, 3, 9))
