def elevator(left, right, call):
    if left == right:
        return 'right'
    elif left == call:
        return 'left'
    elif left < right <= call:
        return 'right'
    elif call < left < right:
        return 'left'
    elif left < right > call:
        return 'right'
    elif right < left < call:
        return 'left'
    elif right < call < left:
        return 'right'
    return 'right'
