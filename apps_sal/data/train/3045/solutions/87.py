def elevator(left, right, call):
    l_distance = abs(call - left)
    r_distance = abs(call - right)
    return 'left' if l_distance < r_distance else 'right'
