def elevator(left, right, call):
    aa = abs(left - call)
    bb = abs(right - call)
    if aa < bb:
        return "left"
    else:
        return "right"
