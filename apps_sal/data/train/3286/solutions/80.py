def enough(cap, on, wait):
    print(cap, on, wait)
    if on + wait > cap:
        return -cap + (on + wait)
    else:
        return 0
