def elevator(left, right, call):
    return abs(call - left) < abs(call - right) and 'left' or 'right'
