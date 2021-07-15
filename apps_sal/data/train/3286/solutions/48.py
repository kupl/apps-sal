def enough(cap, on, wait):
    return -(cap-on-wait) if cap<=on+wait else 0
