def enough(cap, on, wait):
    return wait - (cap - on) if on + wait > cap else 0
