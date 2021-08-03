from heapq import heappush, heappop


def shallowest_path(river):
    ls_o_res, hippo, dc = {}, [], {(i, 0): {} for i in range(len(river))}
    if len(river[0]) > 1:
        for i in range(len(river)):
            dc[(i, 0)][(i, 0)] = ((river[i][0], len([river[i][0]])),
                                  (i, 0), [(i, 0)], [river[i][0]])
            heappush(
                hippo, (((river[i][0], len([river[i][0]])), (i, 0), [(i, 0)], [river[i][0]])))
    else:
        for i in range(len(river)):
            ls_o_res[river[i][0]] = [(i, 0)]
        return ls_o_res[min(ls_o_res.keys())]
    yb, xb = len(river), len(river[0])
    mito = (float("inf"), float("inf"))
    while hippo:
        vara = heappop(hippo)
        moves, parent = [(1, 0), (-1, 0), (0, 1),
                         (1, 1), (-1, 1), (-1, -1), (1, -1), (0, -1)], vara[1]
        for y, x in moves:
            i, j = parent
            i, j = i + y, j + x
            if 0 <= i < yb and 0 <= j < xb:
                path = vara[2] + [(i, j)]
                pathowar = vara[3] + [river[i][j]]
                dist = (max(pathowar), len(pathowar))
                if (i, j) not in dc[(i, 0)]:
                    dc[(i, 0)][(i, j)] = (dist, (i, j), path, pathowar)
                    heappush(hippo, (dist, (i, j), path, pathowar))
                elif (i, j) in dc[(i, 0)] and dist < dc[(i, 0)][(i, j)][0]:
                    dc[(i, 0)][(i, j)] = (dist, (i, j), path, pathowar)
                    heappush(hippo, (dist, (i, j), path, pathowar))
                if j == xb - 1:
                    print(dist)
                    if dist < mito:
                        mito = dist
                        ls_o_res[mito] = path
    return ls_o_res[min(ls_o_res.keys())]
