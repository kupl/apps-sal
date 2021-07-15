def enough(cap, on, wait):
    r = on + wait - cap
    return 0 if r < 0 else r
