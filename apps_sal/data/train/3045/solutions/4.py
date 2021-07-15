def elevator(left, right, call):
    return "right" if abs(right - call) <= abs(left - call) else "left"
