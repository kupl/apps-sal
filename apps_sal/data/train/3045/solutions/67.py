def elevator(left, right, call):
    if call == left and call != right:
        return 'left'
    elif call > left > right or call < left < right:
        return 'left'
    else:
        return 'right'
