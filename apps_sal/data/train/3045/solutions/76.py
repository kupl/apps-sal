def elevator(left, right, call):
    if (abs(call - left) == abs(call - right)) or (abs(call - right) < abs(call - left)):
        return "right"
    else:
        return "left"

