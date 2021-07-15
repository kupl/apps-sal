def squares_needed(grains):
    ct = 0
    i = 0
    while ct < grains:
        ct += 2 ** i
        i += 1
    return i  
