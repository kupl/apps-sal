def enough(cap, on, wait):
    remaining = cap - on
    if remaining >= wait:
        return 0
    else:
        return wait - remaining
