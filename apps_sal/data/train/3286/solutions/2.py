def enough(cap, on, wait):
    return wait + on - cap if wait + on > cap else 0
