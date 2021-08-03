def round_to_next5(n):
    if n == 0 or n % 5 == 0:
        return n
    else:
        n += 5 - (n % 5)
        return n
