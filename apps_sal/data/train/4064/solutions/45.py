def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    product = x * n
    result = list(range(x, product + 1, x))
    return result
