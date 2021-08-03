def elevator(left, right, call):
    if call == right:
        return 'right'
    elif call == left:
        return 'left'
    elif call == left and call == right:
        return 'right'
    elif abs(call - right) < abs(call - left) or abs(call - right) == abs(call - left):
        return 'right'
    else:
        return 'left'
