def round_to_next5(n):
    if n % 5 != 0:
        while n % 5 != 0:
            n += 1
    return n


round_to_next5(-2)
