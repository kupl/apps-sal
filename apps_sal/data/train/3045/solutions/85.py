def elevator(left, right, call):
    if left == right == call:
        return 'right'
    if left == call:
        return 'left'
    if right == call:
        return 'right'
    if abs(left - call) < abs(right - call):
        return 'left'
    else:
        return 'right'
