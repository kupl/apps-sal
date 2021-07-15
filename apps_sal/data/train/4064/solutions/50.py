def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    r = []
    z = 1
    while z <= n:
        y = x * z
        r.append(y)
        z = z + 1
    return r
