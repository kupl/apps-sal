def enough(cap, on, wait):
    c = cap - on
    if(wait <= c):
        return 0
    else:
        return wait - c
