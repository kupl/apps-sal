def find_slope(p):
    y=(p[3]-p[1])
    x=(p[2]-p[0])
    if x==0:
        return "undefined"
    return str(int(y/x))
