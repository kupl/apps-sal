def enough(cap, on, wait):
    enough_space = on + wait - cap
    if enough_space <= 0:
        return 0
    else:
        return enough_space

