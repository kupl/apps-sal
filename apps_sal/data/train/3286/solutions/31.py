def enough(cap, on, wait):
    # Your code here
    c=cap-on
    if(wait<=c):
        return 0
    else:
        return wait-c
