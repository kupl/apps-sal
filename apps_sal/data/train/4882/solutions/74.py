def round_to_next5(n):
    if n % 5 != 0:
        n = n // 5 * 5 + 5
    else:
        n = n
    return n
