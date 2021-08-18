def enough(cap, on, wait):
    n = 0
    if cap >= on + wait:
        return 0
    else:
        n = cap - on - wait
        return abs(n)
