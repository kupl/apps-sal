def enough(cap, on, wait):
    if on + wait <= cap:
        return 0
    else:
        rest = cap - (on + wait)
        return abs(rest)
