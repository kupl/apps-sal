def elevator(left, right, call):
    if abs(left - call) > abs(right - call):
        return 'right'
    elif abs(left - call) < abs(right - call):
        return 'left'
    elif left == right:
        return 'right'
    else:
        return 'right'
