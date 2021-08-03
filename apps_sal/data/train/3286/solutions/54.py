def enough(cap, on, wait):
    num = wait - (cap - on)
    if num >= 0:
        return num
    else:
        return 0
