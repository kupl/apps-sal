def enough(cap, on, wait):
    print(cap, on, wait)
    return 0 if on + wait <= cap else on + wait - cap
