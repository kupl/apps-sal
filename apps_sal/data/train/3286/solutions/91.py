def enough(cap, on, wait):
    total = on + wait
    return 0 if cap >= total else abs(cap - total)
