def enough(cap, on, wait):
    space = cap - on
    return wait - space if space < wait else 0
