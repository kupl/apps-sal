def elevator(left, right, call):
    if left == right or abs(left - call) == abs(right - call):
        return "right"
    elif abs(left - call) < abs(right - call):
        return "left"
    else:
        return "right"
