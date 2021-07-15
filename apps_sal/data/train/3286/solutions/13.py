def enough(cap, on, wait):
    remainingCapacity = cap - on
    if remainingCapacity <= wait:
        return (wait - remainingCapacity)
    else:
        return 0
