def enough(cap, on, wait):
    return (on+wait-cap) * (on + wait > cap)
