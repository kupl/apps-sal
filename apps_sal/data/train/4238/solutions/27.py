def squares_needed(n):
    return 1 + squares_needed(n >> 1) if n else n
