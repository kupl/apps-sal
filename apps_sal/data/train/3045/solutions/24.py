def elevator(left, right, call):
    b = abs(left - call)
    j = abs(right - call)
    if b < j:
        return 'left'
    else:
        return 'right'
