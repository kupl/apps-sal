def elevator(left, right, call):
    distance1 = abs(call - left)
    distance2 = abs(call - right)
    if distance2 <= distance1:
        result = "right"
    else:
        result = "left"
    return result
