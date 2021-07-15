def middle_point(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    x2x3 = x2 <= x1 <= x3 if x2 < x3 else x3 <= x1 <= x2
    y2y3 = y2 <= y1 <= y3 if y2 < y3 else y3 <= y1 <= y2
    z2z3 = z2 <= z1 <= z3 if z2 < z3 else z3 <= z1 <= z2
    x1x3 = x1 <= x2 <= x3 if x1 < x3 else x3 <= x2 <= x1
    y1y3 = y1 <= y2 <= y3 if y1 < y3 else y3 <= y2 <= y1
    z1z3 = z1 <= z2 <= z3 if z1 < z3 else z3 <= z2 <= z1
    x1x2 = x1 <= x3 <= x2 if x1 < x2 else x2 <= x3 <= x1
    y1y2 = y1 <= y3 <= y2 if y1 < y2 else y2 <= y3 <= y1
    z1z2 = z1 <= z3 <= z2 if z1 < z2 else z2 <= z3 <= z1
    if x2x3 and y2y3 and z2z3: return 1
    if x1x3 and y1y3 and z1z3: return 2
    if x1x2 and y1y2 and z1z2: return 3

