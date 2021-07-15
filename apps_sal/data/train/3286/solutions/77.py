def enough(cap, on, wait):
    a = cap - on - wait
    if a >= 0: return 0
    else: return a * -1
