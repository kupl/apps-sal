def elevator(left, right, call):
    if left == call and call != right:
        return "left"
    elif right == call and call != left:
        return "right"
    if abs(left - call) < abs(right - call):
        return "left"
    elif abs(left - call) > abs(right - call):
        return "right"
    return "right"
