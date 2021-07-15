def enough(cap, on, wait):
    return 0 if wait < cap - on else -(cap-on-wait)
