def elevator(left, right, call):
    return 'right' if right == left == call or abs(call - right) <= abs(call - left) else 'left'
