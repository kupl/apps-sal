from math import cos, hypot, pi, sin
from string import ascii_uppercase


def web_to_xy(c):
    radial, ring = c
    r = int(ring)
    angle = ascii_uppercase.find(radial) * pi / 4
    return r * cos(angle), r * sin(angle)


def spider_to_fly(spider, fly):
    sx, sy = web_to_xy(spider)
    fx, fy = web_to_xy(fly)
    return round(hypot(sx - fx, sy - fy), 6)
