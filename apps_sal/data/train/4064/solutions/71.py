def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    res = []
    c = 0
    for i in range(n):
        c += x
        res.append(c)
    return res
