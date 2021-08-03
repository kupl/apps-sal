def enough(cap, on, wait):
    if wait <= cap - on:
        return 0
    else:
        return abs(wait - (cap - on))
