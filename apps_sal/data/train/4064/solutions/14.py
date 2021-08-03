def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    output = []
    i = 1
    while len(output) < n:
        output.append(i * x)
        i += 1
    return output
