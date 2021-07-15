def bar_triang(pa, pb, pc):
    xa, ya = pa
    xb, yb = pb
    xc, yc = pc
    xO = round((xa + xb + xc) / 3, 4)
    yO = round((ya + yb + yc) / 3, 4)
    return [xO, yO]
