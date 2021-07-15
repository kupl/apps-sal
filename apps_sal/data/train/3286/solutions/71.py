def enough(cap, on, wait):
    if cap == on + wait or cap > on + wait:
        return 0
    else:
        return abs(cap - (on + wait))
