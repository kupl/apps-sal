def enough(cap, on, wait):
    return 0 if wait + on <= cap - 1 else wait + on - (cap)
