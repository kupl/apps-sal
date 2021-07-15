def enough(cap, on, wait):
    free = cap-on
    return 0 if free >= wait else wait-free

