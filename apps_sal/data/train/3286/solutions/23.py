def enough(cap, on, wait):
    num = cap - on
    if num == wait:
        return 0
    if wait > num:
        return (wait - num)
    else:
        return 0
