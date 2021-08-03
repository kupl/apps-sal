def elevator(left, right, call):
    "return closest elevator"
    return "left" if abs(left - call) < abs((right - call)) else "right"
