def elevator(left, right, call):
    a = abs(call - left)
    b = abs(call - right)
    return 'left' if b > a else 'right'
