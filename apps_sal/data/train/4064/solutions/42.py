def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    lis = []
    i = 1
    while len(lis) < n:
        if i % x == 0:
            lis.append(i)
        i += 1

    return lis
