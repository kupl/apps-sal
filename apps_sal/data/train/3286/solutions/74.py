def enough(cap, on, wait):
    available = cap - on
    return max(wait - available, 0)
