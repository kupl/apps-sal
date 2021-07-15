def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    array = []
    number = 0
    m = x
    while number < n:
        array.append(m)
        m += x
        number += 1
    return array
