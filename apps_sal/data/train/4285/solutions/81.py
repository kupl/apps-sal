def find_slope(p):
    return str(int((p[3] - p[1]) / (p[2] - p[0]))) if p[2] != p[0] else 'undefined'
