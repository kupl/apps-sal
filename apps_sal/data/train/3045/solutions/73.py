def elevator(left, right, call):
    if call == left and call == right:
        return 'right'
    elif call == left:
        return 'left'
    elif call == right:
        return 'right'
    elif left == right:
        return 'right'
    else:
        return 'left' if abs(call - left) < abs(call - right) else 'right'
