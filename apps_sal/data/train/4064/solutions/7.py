def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    my_list = []
    for number in range(1, n + 1):
        my_list.append(x*number)
    return my_list
