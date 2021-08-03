def enough(cap, on, wait):
    if wait > cap - on:
        return wait + on - cap
    else:
        return 0
