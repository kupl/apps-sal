def elevator(left, right, call):
    if right == call:
        return 'right'
    elif left == call:
        return 'left'
    elif abs(right - call) == 1:
        return 'right'
    elif abs(left - call) == 1:
        return 'left'
    else:
        return 'right'
