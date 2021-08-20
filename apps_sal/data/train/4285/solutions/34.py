def find_slope(p):
    if p[0] == p[2]:
        return 'undefined'
    else:
        return str(int((p[1] - p[3]) / (p[0] - p[2])))
