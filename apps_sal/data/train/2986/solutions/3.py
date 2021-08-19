def segments(m, a):
    occupied = []
    for i in a:
        for x in range(i[0], i[1] + 1):
            occupied.append(x)
    free = []
    for n in range(0, m + 1):
        if n not in occupied:
            free.append(n)
    return free
