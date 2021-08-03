def elevator(left, right, call):
    return "left" if (call - left) * (call - left) < (call - right) * (call - right) else "right"
