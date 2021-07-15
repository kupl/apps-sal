def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    res = []
    num = x
    while n > 0:
        res.append(num)
        num += x
        n -= 1
    return res

