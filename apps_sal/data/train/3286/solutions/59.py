def enough(cap, on, wait):
    if cap-on+1>wait: return 0
    else:return wait-cap+on
