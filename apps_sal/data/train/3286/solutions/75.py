def enough(cap, on, wait):
    return 0 if cap - on - wait > 0 else (cap - on - wait) * -1
