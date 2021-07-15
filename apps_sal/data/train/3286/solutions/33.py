def enough(cap, on, wait):
    empty = cap - on
    return 0 if empty >= wait else wait - empty
