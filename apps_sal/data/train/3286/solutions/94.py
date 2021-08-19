def enough(cap, on, wait):
    return 0 if cap % (on + wait) == 0 or on + wait < cap else on + wait - cap
