def round_to_next5(n):
    roundup = 5 - n % 5
    if n % 5 == 0:
        return n
    else:
        return n + roundup
