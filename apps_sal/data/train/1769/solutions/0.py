from collections import defaultdict


def shortestPath(gra, srs, des):
    Q, paths, d = [[0, srs]], [], defaultdict(list)
    while Q:
        vrt = Q.pop(0)
        if vrt[-1] == des:
            paths.append(vrt)
            continue
        for v, c in gra[vrt[-1]].items():
            if v not in vrt:
                Q.append([vrt[0] + c] + vrt[1:] + [v])

    for i in paths:
        d[i[0]].append(i[1:])

    ml, f = len(min(d[min(d)], key=len)), []

    for i in d[min(d)]:
        if len(i) == ml:
            f.append(i)
    return [sorted(i) for i in f] if len(f) > 2 else f
