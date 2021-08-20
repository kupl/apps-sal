def elevator(left, right, call):
    if abs(call - left) < abs(call - right):
        return 'left'
    if abs(call - left) > abs(call - right):
        return 'right'
    return 'right'
