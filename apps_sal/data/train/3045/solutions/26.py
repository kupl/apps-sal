def elevator(left, right, call):
    left_dist = abs(call - left)
    right_dist = abs(call - right)

    if left_dist >= right_dist:
        return 'right'
    else:
        return 'left'
