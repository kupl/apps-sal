def find_slope(p):
    x = p[0] - p[2]
    y = p[1] - p[3]
    if x != 0:
        return str(int(y / x))
    else:
        return 'undefined'
