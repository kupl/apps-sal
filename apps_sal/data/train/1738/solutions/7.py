def biggest_triang_int(points, ce, ra):
    max = 0
    r = []
    le = len(points)
    count = 0
    for i in range(le):
        for j in range(i + 1, le):
            for k in range(j + 1, le):
                po = [points[i], points[j], points[k]]
                if distance(po[0], ce) <= ra and distance(po[1], ce) <= ra and (distance(po[2], ce) <= ra):
                    count += 1
                    ae = areatriangle(po[0], po[1], po[2])
                    if ae >= max:
                        if abs(ae - max) > 1e-05:
                            max = ae
                            r = [po]
                        else:
                            r.append(po)
    if len(r) == 1:
        r = r[0]
    return [count, max, r] if count > 0 else []


def areatriangle(xxx_todo_changeme, xxx_todo_changeme1, xxx_todo_changeme2):
    (x1, y1, z1) = xxx_todo_changeme
    (x2, y2, z2) = xxx_todo_changeme1
    (x3, y3, z3) = xxx_todo_changeme2
    a = distance((x1, y1, z1), (x2, y2, z2))
    b = distance((x2, y2, z2), (x3, y3, z3))
    c = distance((x3, y3, z3), (x1, y1, z1))
    return heron(a, b, c)


def heron(a, b, c):
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


def distance(xxx_todo_changeme3, xxx_todo_changeme4):
    (x1, y1, z1) = xxx_todo_changeme3
    (x2, y2, z2) = xxx_todo_changeme4
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5
