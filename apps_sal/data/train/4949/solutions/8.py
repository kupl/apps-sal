from math import cos, sin, radians as rad

def crusoe(n, d, a, dd, da):
    x=y=0
    for _ in range(n):
        x += d * cos(rad(a))
        y += d * sin(rad(a))
        d, a = d*dd, a*da
    return (x, y)
