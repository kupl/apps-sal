def elevator(left, right, call):
    distance_left = abs(call - left)
    distance_right = abs(call - right)
    if distance_right <= distance_left or right == call:
        return "right"
    else:
        return "left"
