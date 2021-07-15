def enough(cap, on, wait):
    x = on + wait
    if x <= cap:
        return 0
    elif x > cap:
        return x - cap
    else:
        return 'Not Sure'

