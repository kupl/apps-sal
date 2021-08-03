def elevator(left, right, call):
    a, b = abs(call - right), abs(call - left)
    if a <= b:
        return 'right'
    return 'left'
