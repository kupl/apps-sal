def enough(cap, on, wait):
    if cap < on + wait:
        return wait-(cap-on)
    else:
        return 0
