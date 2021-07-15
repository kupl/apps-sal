def enough(cap, on, wait):
    return abs(on + wait - cap) if cap < on + wait else 0
