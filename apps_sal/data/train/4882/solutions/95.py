def round_to_next5(n):
    if n % 5 == 0:
        return n
    n = n - n % 5 + 5
    return n
