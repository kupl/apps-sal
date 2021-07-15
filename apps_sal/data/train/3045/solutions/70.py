def elevator(left, right, call):
    if right == call or abs(call-right) <= abs(call-left):
        return 'right' 
    return 'left'
