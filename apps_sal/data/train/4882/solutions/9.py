def round_to_next5(n):
    (x, y) = divmod(n, 5)
    return (x + (y > 0)) * 5
