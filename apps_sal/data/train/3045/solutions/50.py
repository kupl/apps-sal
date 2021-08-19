def elevator(left, right, call):
    if left == right:
        return 'right'
    elif left == 0 and call == 0:
        return 'left'
    elif left == 1 and call == 1:
        return 'left'
    elif left == 2 and call == 2:
        return 'left'
    elif left == 1 and call == 2 and (right == 0):
        return 'left'
    elif left == 1 and call == 0 and (right == 2):
        return 'left'
    else:
        return 'right'
