def enough(cap, on, wait):
    if on + wait > cap:
        missed_out = on + wait - cap
    else:
        missed_out = 0
    return missed_out
