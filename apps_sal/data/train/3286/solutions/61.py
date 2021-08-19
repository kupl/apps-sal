def enough(cap, on, wait):
    c = cap - on
    if c < wait:
        return wait - c
    return 0
