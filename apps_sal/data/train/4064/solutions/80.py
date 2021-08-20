def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    new_list = []
    y = 0
    for count in range(n):
        new_list.append(y + x)
        y = y + x
    return new_list
