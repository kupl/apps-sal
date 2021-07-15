from math import cos,sin,radians

def coordinates(d, r):
    convert = lambda x: round(r*x(radians(d)),10)
    return ( convert(cos), convert(sin) )
