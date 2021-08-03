def find_slope(p):
    y = (p[1] - p[3])
    x = (p[0] - p[2])
    if x == 0:
        return "undefined"
    else:
        return "{}".format(int(y / x))
