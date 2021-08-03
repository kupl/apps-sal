def elevator(left, right, call):
    d_left = left - call
    d_right = right - call
    if (d_left + d_right == 0 or abs(d_left) > abs(d_right) or d_left == d_right):
        return "right"
    else:
        return "left"
