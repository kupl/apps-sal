def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    new_list = []
    tracker = 1

    while tracker <= n:
        new_list.append(tracker * x)
        tracker += 1

    return new_list
