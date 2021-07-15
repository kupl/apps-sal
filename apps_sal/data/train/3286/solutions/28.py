def enough(cap, on, wait):
    return wait - (cap-on) if wait - (cap-on) >= 0 else 0
