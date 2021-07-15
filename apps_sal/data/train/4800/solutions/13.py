def hotpo(n: int) -> int:
    """ Get the number of times you need to perform this algorithm to get n = 1. """
    seq = []
    while n > 1:
        if not n % 2:
            n = n / 2
        else:
            n = 3 * n + 1
        seq.append(n)
    return len(seq)
