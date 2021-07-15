def elevator(left, right, call):
    if left == right:
        return 'right'
    return 'right' if -abs(call - left) <= -abs(call - right) else 'left'
