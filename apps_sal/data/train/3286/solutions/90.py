def enough(cap, on, wait):
    n = on + wait
    if cap > n:
        return 0
    return on + wait - cap
