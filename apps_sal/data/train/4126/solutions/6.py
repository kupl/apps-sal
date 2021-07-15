import math
def what_time_is_it(angle):
    mins=2*(angle%360)
    h=math.floor(mins/60) or 12
    m=math.floor(mins%60)
    return '{:02}:{:02}'.format(h,m)
