def enough(cap, on, wait):
    return 0 if cap >= on + wait else on + wait - cap
