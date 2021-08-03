def enough(cap, on, wait):
    cap -= on
    if wait - cap <= 0:
        return 0
    else:
        return wait - cap
