def enough(cap, on, wait):
    if cap - on >= wait:
        return 0
    else:
        return wait - cap + on
