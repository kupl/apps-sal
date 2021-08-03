def enough(cap, on, wait):
    return abs(cap - (on + wait) if cap < (on + wait) else 0)
