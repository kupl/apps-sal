def dropzone(p, dropzones):
    res = []
    x1, y1 = p[0], p[1]
    for dropzone in dropzones:
        x2, y2 = dropzone[0], dropzone[1]
        dist = ((x2-x1)**2 + (y2-y1)**2)**.5
        res.append(dist)
    shortest = res.index(min(res))
    return dropzones[shortest]
