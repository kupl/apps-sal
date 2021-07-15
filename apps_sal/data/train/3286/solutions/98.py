def enough(cap, on, wait):
    a = on + wait
    b = cap - a 
    if b >= 0:
        return 0
    else:
        return abs(b)
