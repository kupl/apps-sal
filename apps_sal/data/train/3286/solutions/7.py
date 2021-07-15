def enough(cap, on, wait):
    return max(wait + on - cap, 0)
