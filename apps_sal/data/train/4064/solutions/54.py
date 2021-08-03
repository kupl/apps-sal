def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    y = x
    df = []
    i = 1
    while i < n + 1:
        x = x
        df.append(x)
        x = x + y
        i += 1
    return df
