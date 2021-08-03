def elevator(left, right, call):
    delta_left = abs(left - call)
    delta_right = abs(right - call)
    if delta_left < delta_right:
        return 'left'
    else:
        return 'right'
