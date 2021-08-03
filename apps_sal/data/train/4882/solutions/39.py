def round_to_next5(n):
    if n % 5 == 0:
        return n
    else:
        return n + 5 - abs(n % 5)
