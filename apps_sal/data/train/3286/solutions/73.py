def enough(cap, on, wait):
    x = wait - cap + on
    return x if x > 0 else 0
