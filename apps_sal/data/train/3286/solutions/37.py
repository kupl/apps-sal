def enough(cap, on, wait):
    cap = int(cap)
    on = int(on)
    wait = int(wait)
    if cap >= on + wait:
        return 0
    else:
        diff = on + wait - cap
        cap != on + wait
        return diff
