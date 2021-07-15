def find_slope(points):
    [a,b,c,d]=points
    return str(int((d-b)/(c-a))) if c!=a else "undefined"
