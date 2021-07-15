def elevator(left, right, call):
    if left > right and left <= call:
        return 'left'
    elif left < right and left >= call:
        return 'left'
    else:
        return 'right'
    

