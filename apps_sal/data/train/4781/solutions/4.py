from math import cos, radians, sin


def spider_to_fly(spider, fly):
    (ts, rs), (tf, rf) = ((radians((ord(c) - 65) * 45), int(n)) for c, n in (spider, fly))
    return ((rs * cos(ts) - rf * cos(tf))**2 + (rs * sin(ts) - rf * sin(tf))**2)**0.5
