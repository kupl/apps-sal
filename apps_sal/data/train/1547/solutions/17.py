d1, v1, d2, v2, p = input().split()
d1 = int(d1)
v1 = int(v1)
d2 = int(d2)
v2 = int(v2)
p = int(p)
if d1 == d2:
    if p % (v1 + v2) == 0:
        rd = int(p / (v1 + v2)) + d1 - 1
    else:
        rd = int(p // (v1 + v2)) + d1
elif d1 < d2:
    dd = d2 - d1
    vp = v1 * dd
    if p <= dd:
        if p % v1 == 0:
            rd = int(p / v1) + d1 - 1
        else:
            rd = int(p // v1) + d1
    else:
        vl = p - vp
        if vl % (v1 + v2) == 0:
            rd = int(vl / (v1 + v2)) + d2 - 1
        else:
            rd = int(vl // (v1 + v2)) + d2
else:
    dd = d1 - d2
    vp = v2 * dd
    if p <= vp:
        if p % v2 == 0:
            rd = int(p / v2) + d2 - 1
        else:
            rd = int(p // v2) + d2
    else:
        vl = p - vp
        if vl % (v1 + v2) == 0:
            rd = int(vl / (v1 + v2)) + d1 - 1
        else:
            rd = int(vl // (v1 + v2)) + d1
print(rd)
