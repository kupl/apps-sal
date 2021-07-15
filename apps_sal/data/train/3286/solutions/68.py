def enough(cap, on, wait):
    rest = on + wait - cap
    if rest <= 0:
        return 0
    return rest
