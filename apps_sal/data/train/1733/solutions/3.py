from collections import deque
MOVES = [[1, -2], [1, 2], [2, -1], [2, 1], [-1, -2], [-1, 2], [-2, 1], [-2, -1]]


def knight(p1, p2):
    p1 = (8 - int(p1[1]), 'abcdefgh'.index(p1[0]))
    p2 = (8 - int(p2[1]), 'abcdefgh'.index(p2[0]))

    Q = deque([(p1, -1)])
    visited = set()

    while Q:
        k, l = Q.popleft()
        l += 1
        visited.add(k)

        if k == p2:
            return l

        for i, j in MOVES:
            ni, nj = k[0] + i, k[1] + j
            if 0 <= ni < 8 and 0 <= nj < 8 and (ni, nj) not in visited:
                Q.append([(ni, nj), l])
    return None
