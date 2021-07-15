def elevator(left, right, call):
    return "left" if abs(left - call) < abs(right - call) else "right"
