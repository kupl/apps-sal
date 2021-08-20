def how_many_measurements(n):
    exp = 0
    while 3 ** exp < n:
        exp += 1
    return exp
