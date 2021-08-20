def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    result = (x * z for z in range(1, n + 1))
    '\n    for z in range(1,n+1):\n        result.append(x*z)\n    '
    return list(result)
