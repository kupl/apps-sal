def enough(cap, on, wait):
    if on >= cap:
        return wait
    spots = cap - on
    if spots >= wait:
        return 0
    return wait - spots


