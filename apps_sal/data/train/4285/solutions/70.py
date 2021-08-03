def find_slope(a):
    x1, x2 = a[0], a[2]
    y1, y2 = a[1], a[3]
    if x1 != x2:
        return str(int((y2 - y1) / (x2 - x1)))
    else:
        return "undefined"
