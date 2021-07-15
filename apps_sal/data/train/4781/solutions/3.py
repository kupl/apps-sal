import math as m
import string as str

def spider_to_fly(spider, fly):
    if (spider == fly):
        return 0
    else:
        angle = get_angle(spider[0], fly[0])
        s_dist = int(spider[1])
        f_dist = int(fly[1])
        return m.sqrt((s_dist**2)+(f_dist**2)-2*s_dist*f_dist*m.cos(m.radians(angle)))


def get_angle(s, f):
    s_angle = (str.ascii_uppercase.index(s)) * 45
    f_angle = (str.ascii_uppercase.index(f)) * 45
    return abs(s_angle - f_angle)
