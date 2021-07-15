def elevator(left, right, call):
    if abs(left - call) < abs(right - call):
        result = 'left'
    else:
        result = 'right'
    return result
