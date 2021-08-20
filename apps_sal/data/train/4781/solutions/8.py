from math import sqrt, cos, radians


def spider_to_fly(spider, fly):
    rad = radians((ord(spider[0]) - ord(fly[0])) % 8 * 45)
    (a, b) = (int(spider[1:]), int(fly[1:]))
    return sqrt(a ** 2 + b ** 2 - 2 * a * b * cos(rad))
