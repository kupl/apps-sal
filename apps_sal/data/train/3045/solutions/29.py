def elevator(left, right, call):
    r_dist = call - right
    l_dist = call - left
    if r_dist < 0:
        r_dist *= -1
    if l_dist < 0:
        l_dist *= -1

    if r_dist <= l_dist:
        return 'right'
    else:
        return 'left'
