def elevator(left, right, call):
    if left == right and left == call:
        return 'right'
    if call == left:
        return 'left'
    if call == right:
        return 'right'
    if abs(call - left) < abs(call - right):
        return 'left'
    else:
        return 'right'
