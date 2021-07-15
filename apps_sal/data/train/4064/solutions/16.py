def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    lst = []
    y = 0
    while len(lst) < n:
        y += x
        lst.append(y)
    return lst
