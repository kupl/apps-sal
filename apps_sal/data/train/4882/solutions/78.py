def round_to_next5(n):
    if n % 5 == 0:
        return n
    else:
        to_add = 5 - n % 5
        return n + to_add
