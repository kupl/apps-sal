def enough(cap, on, wait):
    cant = cap - wait
    if on + wait > cap:
        a = cap - on - wait
        return abs(a)
    else:
        return 0
