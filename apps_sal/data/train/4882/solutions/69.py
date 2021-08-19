def round_to_next5(n):
    x = n % 5
    if x == 0:
        y = n
    else:
        y = n + (5 - x)
    return y
