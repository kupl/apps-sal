def enough(cap, on, wait):
    if wait > cap - on:
        return on + wait - cap
    return 0
