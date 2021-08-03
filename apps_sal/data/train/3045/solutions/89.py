def elevator(left, right, call):
    if left == right:
        return 'right'
    elif left == call:
        return 'left'
    elif call - right == 1 or right - call == 1 or call == right:
        return 'right'
    else:
        return 'left'
