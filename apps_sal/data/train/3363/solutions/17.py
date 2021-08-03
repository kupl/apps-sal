def evaporator(c, e, t):
    tc = 100
    count = 0
    while tc > t:
        tc -= tc * (e / 100)
        count += 1
    return count
