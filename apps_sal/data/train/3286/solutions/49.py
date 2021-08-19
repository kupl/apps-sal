def enough(cap, on, wait):
    c = cap - on - wait
    if c == 0:
        return 0
    if c > 0:
        return 0
    else:
        return c * -1
