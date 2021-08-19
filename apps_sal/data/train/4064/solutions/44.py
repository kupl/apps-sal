def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    count = []
    total = 0
    while n > 0:
        total += x
        count.append(total)
        n -= 1
    return count
