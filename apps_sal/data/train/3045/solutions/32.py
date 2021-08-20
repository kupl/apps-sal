def elevator(left, right, call):
    el1 = abs(call - right)
    el2 = abs(call - left)
    if el1 > el2:
        return 'left'
    else:
        return 'right'
