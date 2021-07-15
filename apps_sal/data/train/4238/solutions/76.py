def squares_needed(grains):
    n = 0
    needed = 0
    while grains > needed:
        needed+= 2**n
        n+=1
    return n
