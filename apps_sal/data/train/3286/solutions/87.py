def enough(cap, on, wait):
    cap -= on
    return max(wait - cap, 0)
