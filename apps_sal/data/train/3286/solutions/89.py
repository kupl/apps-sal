def enough(cap, on, wait):
    return 0 if cap-on-wait>0 else abs(cap-on-wait) if cap-on-wait<0 else 0
