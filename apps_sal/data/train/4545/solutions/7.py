import math

PI = math.pi

def build_cutoffs():
    angle = PI/10
    start = PI/20
    cutoffs = [start]
    for i in range(1,20):
        cutoffs.append(start + angle)
        start+=angle
    return cutoffs

hitvals = [6, 13, 4, 18, 1, 20, 5, 12, 9, 14, 11, 8, 16, 7, 19, 3, 17, 2, 15, 10]
num_cutoffs = build_cutoffs()

def calc_angle(x,y):
    oa = y/x
    taninv = math.atan(abs(oa))
    if oa > 0:
        radang = PI + taninv if y<0 else taninv
    else:
        radang = PI - taninv if x < 0 else 2*PI - taninv
    return radang

def get_score(x,y):
    ang = calc_angle(x,y)
    for i, c in enumerate(num_cutoffs):
        if ang < c:
            numval = hitvals[i]
            break
    else:
        numval = 6

    dist = math.sqrt(x**2 + y**2)
    if dist > 170:
        return 'X'
    if dist > 162:
        return f'D{numval}'
    if dist > 99 and dist < 107:
        return f'T{numval}'
    if dist > 6.35 and dist < 15.9:
        return 'SB'
    if dist < 6.35:
        return 'DB'
    return f'{numval}'
