def enough(cap, on, wait):
    # Your code here
    c=cap-on
    if c<wait:
        return wait-c
    return 0
