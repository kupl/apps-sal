def enough(cap, on, wait):
    x = cap - on - wait
    return x * -1 if x <= 0 else 0
