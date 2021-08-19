def elevator(left, right, call):
    return 'left' if abs(right - call) > abs(left - call) else 'right'
