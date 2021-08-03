def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """

    list = []
    y = x

    while len(list) < n:
        list.append(y)
        y += x

    return list
