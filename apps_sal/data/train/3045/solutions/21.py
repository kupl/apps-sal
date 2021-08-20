def elevator(left, right, call):
    closest = 'left'
    if abs(right - call) <= abs(left - call):
        closest = 'right'
    return closest
