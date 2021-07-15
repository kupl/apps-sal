def enough(cap, on, wait):
    x = cap - on
    if x >= wait:
        return 0
    else:
        return wait - x
