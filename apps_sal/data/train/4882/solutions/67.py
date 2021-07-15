def round_to_next5(n):
    while int(n) % 5 != 0:
        n = int(n) + 1
    return n
