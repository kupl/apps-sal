def to_1D(x, y, s):
    return s[0]*y + x
def to_2D(n, s):
    return (n // s[0], n % s[0])[::-1]
