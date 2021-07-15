from numpy import angle, abs, exp, pi

def spider_to_fly(*creatures):
    a, b = (int(x[1]) * exp( -1j * (ord(x[0])-3)/4.0*pi ) for x in creatures)
    return abs(a-b)

