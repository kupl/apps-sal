def elevator(left, right, call):
    if right == call and call == left:
        return 'right'
    elif right == call:
        return 'right'
    elif left == call:
        return 'left'
    elif left > right and right > call:
        return 'right'
    elif right > left and left > call:
        return 'left'
    elif right - call >= left - call:
        return 'right'
    elif call - right <= call - left:
        return 'left'
    elif call > left and left > right:
        return 'left'
    elif left > call and call > right:
        return 'right'
