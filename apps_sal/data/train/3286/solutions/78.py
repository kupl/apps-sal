def enough(cap, on, wait):
    r = cap - on - wait
    return [0, abs(r)][r < 0]
