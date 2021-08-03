def avg_diags(m):
    prim = []
    sec = []
    for i in range(len(m)):
        prim.append(m[i][i])
        sec.append(m[i][-i - 1])
    sec.reverse()

    prim = [prim[i] for i in range(len(prim)) if i % 2 != 0 and prim[i] >= 0]
    sec = [sec[i] for i in range(len(sec)) if i % 2 == 0 and sec[i] <= 0]

    prim = round(sum(prim) / len(prim))
    if len(sec) == 0:
        sec = -1
        return[prim, sec]
    else:
        sec = round(sum(sec) / len(sec))
    if sec < 0:
        sec = -sec
    return [prim, sec]
