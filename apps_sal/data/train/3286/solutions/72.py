def enough(cap, on, wait):
    takes = cap - on - wait
    return 0 if takes >= 0 else -takes
