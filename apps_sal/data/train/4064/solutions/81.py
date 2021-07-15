def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    i = 1
    rl = []
    while i <= n:
        rl.append(i*x)
        i += 1
    return rl
