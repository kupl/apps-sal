def find_slope(p):
    if p[2] == p[0]:
        return "undefined"
    else:
        return str((p[3]-p[1])//(p[2]-p[0]))

