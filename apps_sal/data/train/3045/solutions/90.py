def elevator(left, right, call):
    x, y = abs(call - right), abs(call - left)
    if x > y:
        return "left"
    elif x == y:
        return "right"
    else:
        return "right"
    pass  # Code on! :)
