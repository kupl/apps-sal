from math import cos, pi

def spider_to_fly(a, b):
    x, y = int(a[1]), int(b[1])
    return (x**2 + y**2 - 2 * x * y * cos((ord(a[0]) - ord(b[0])) * pi / 4))**0.5
