def elevator(left, right, call):
    leftDiff = abs(call-left)
    rightDiff = abs(call-right)
    if leftDiff > rightDiff: 
        return 'right'
    elif leftDiff < rightDiff: 
        return 'left'
    else: 
        return 'right'
