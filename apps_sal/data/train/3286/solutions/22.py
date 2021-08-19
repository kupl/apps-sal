def enough(cap, on, wait):
    c = wait - (cap - on)
    if c < 0:
        return 0
    return c
