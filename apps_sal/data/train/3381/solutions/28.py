def get_real_floor(n: int) -> int:
    """ Get the floor in the european system based on the floor in the american system. """
    return sum([n, {0 < n < 13: -1, n >= 13: -2}.get(True, 0)])
