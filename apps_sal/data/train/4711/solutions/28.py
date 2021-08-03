def zeros(n):

    # Initialize result
    count = 0

    # Keep dividing n by
    # powers of 5 and
    # update Count
    i = 5
    while (n / i >= 1):
        count += int(n / i)
        i *= 5

    return int(count)
