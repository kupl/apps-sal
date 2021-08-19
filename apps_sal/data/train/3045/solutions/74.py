def elevator(left, right, call):
    if abs(right - call) == abs(left - call):
        return 'right'
    else:
        return 'right' if abs(right - call) < abs(left - call) else 'left'
