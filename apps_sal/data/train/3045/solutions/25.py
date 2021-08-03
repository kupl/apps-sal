def elevator(left, right, call):
    print((left, right, call))
    if call == left and call != right:
        return 'left'
    elif call == right and call != left:
        return 'right'
    elif abs(right - call) < abs(left - call):
        return 'right'
    elif abs(right - call) > abs(left - call):
        return 'left'
    elif abs(right - call) == abs(left - call):
        return 'right'
