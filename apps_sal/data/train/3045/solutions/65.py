def elevator(left, right, call):
    if left == right:
        return 'right'
    elif abs(call - right) < abs(call - left):
        return 'right'
    elif abs(call - left) < abs(call - right):
        return 'left'
    elif abs(call - left) == abs(call - right):
        return 'right'
