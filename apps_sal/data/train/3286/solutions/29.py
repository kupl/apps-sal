def enough(cap, on, wait):
    cap_lef = cap - on
    still_wait = wait - cap_lef
    if still_wait > 0:
        return still_wait
    else:
        return 0
