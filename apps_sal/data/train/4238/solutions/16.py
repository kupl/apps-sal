def squares_needed(grains):
    n = 0
    while sum(2**i for i in range(n)) < grains:
        n += 1
    return n
        

