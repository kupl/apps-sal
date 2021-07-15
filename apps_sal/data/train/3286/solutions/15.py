def enough(cap, on, wait):
    return 0 if cap - on >= wait else wait - cap + on
