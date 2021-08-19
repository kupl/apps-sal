def round_to_next5(n):
    if n % 5 == 0:
        return n
    while True:
        if (n + 1) % 5 == 0:
            return n + 1
        n += 1
    return n
