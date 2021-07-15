def round_to_next5(n):
    remainder = 1
    while remainder != 0:
        remainder = n % 5
        n += 1
    return n - 1
