def enough(cap, on, wait):
    difference = cap - on
    if difference < wait:
        return wait - difference
    return 0
