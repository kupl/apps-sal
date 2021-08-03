def enough(cap, on, wait):
    if on + wait > cap:
        return (cap - (on + wait)) * -1
    return 0
