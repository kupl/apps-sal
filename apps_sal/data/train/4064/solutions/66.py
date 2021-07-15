def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    if x == 1:
        return [x for x in range(x, n+1)]
    else:
        y = [x, (n*x)]
        z = []
        for j in range(1, n+1):
            z.append(y[0]*j)
        return z

