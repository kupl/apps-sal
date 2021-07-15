def elevator(left, right, call):
    x = call - left
    y = call - right
    if (left == call and right != call) or (right < left < call) or (call < left < right):
        return 'left'
    return 'right'

