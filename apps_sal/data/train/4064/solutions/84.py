def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    w = []
    k = 0
    for i in range(n):
        k = k + x
        w.append(k)
    return w

