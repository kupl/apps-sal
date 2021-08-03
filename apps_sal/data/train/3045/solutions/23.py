def elevator(left, right, call):
    return 'right' if abs(left - call) == abs(right - call) else 'left' if abs(left - call) < abs(right - call) else 'right'
