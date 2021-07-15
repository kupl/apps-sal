def enough(cap, on, wait):
    return abs(min(cap - on - wait, 0))
