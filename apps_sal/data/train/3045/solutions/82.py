def elevator(left, right, call):
    isLeft = abs(call - left) < abs(call - right)
    return "left" if isLeft else "right"
