def elevator(left, right, call):
    if left == call and right != call or abs(call - left) < abs(call - right):
        return 'left'
    return 'right'
