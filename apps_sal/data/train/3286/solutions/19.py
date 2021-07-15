def enough(cap, on, wait):
    a=cap-on
    if a>=wait:
        return 0
    else:
        b=wait-a
        return b
