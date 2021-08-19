def elevator(left, right, call):
    d = abs(left - call)
    s = abs(right - call)
    if d < s:
        return 'left'
    else:
        return 'right'
