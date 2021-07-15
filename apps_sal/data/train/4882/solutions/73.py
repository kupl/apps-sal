def round_to_next5(n):
    if n % 5 == 0 or n == 0:
        return n
    else:
        while(not n % 5 == 0):
            n += 1
    return n
