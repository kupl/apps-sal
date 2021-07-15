def enough(cap, on, wait):
    # Your code here
    diff = cap-on-wait
    return 0 if diff >=0 else -diff
