def elevator(left, right, call):
    r = abs(right - call)
    l = abs(left - call)
    return 'right' if r <= l else 'left'
