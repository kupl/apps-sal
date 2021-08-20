def elevator(left, right, call):
    return 'right' if abs(call - right) <= abs(call - left) else 'left'
