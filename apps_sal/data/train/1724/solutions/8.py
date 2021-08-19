def blast_sequence(aliens, position):
    dal = []
    wdh = len(aliens[0])
    for y in range(len(aliens)):
        for x in range(len(aliens[y])):
            if aliens[y][x] != 0:
                dal.append((y, x, aliens[y][x]))
    yp, xp = position
    hgh = yp + 1
    dr = []
    i = -1
    while len(dal) > 0:
        i += 1
        ddel = []
        for k in range(len(dal)):
            y, x, v = dal[k]
            # print(y, x, v)
            x += v
            if x < 0:
                v = -v
                x = -x - 1
                y += 1
                if y == yp:
                    return None
            elif x >= wdh:
                v = -v
                x = wdh + wdh - 1 - x
                y += 1
                if y == yp:
                    return None
            dal[k] = (y, x, v)
            if x == xp:
                ddel.append(k)
        if len(ddel) > 0:
            ymax = 0
            for k in ddel:
                y, x, v = dal[k]
                ymax = max(ymax, y)
            ddel2 = []
            for k in ddel:
                y, x, v = dal[k]
                if y == ymax:
                    ddel2.append(k)
            if len(ddel2) == 1:
                kdel = ddel2[0]
            else:
                vmax = 0
                for k in ddel2:
                    y, x, v = dal[k]
                    vmax = max(vmax, abs(v))
                ddel = []
                for k in ddel2:
                    y, x, v = dal[k]
                    if abs(v) == vmax:
                        ddel.append(k)
                if len(ddel) == 1:
                    kdel = ddel[0]
                else:
                    for k in ddel:
                        y, x, v = dal[k]
                        if v > 0:
                            kdel = k
                            break
            dr.append(i)
            dal.pop(kdel)
    return dr
