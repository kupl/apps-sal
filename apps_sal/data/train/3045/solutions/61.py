def elevator(left, right, call):
    leftdist = abs(left - call)
    rightdist = abs(right - call)
    if leftdist == rightdist:
        return 'right'
    elif leftdist > rightdist:
        return 'right'
    else:
        return 'left'
