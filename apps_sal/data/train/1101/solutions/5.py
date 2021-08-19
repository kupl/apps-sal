# cook your dish here
import collections
from itertools import combinations


def checkintersection(e1, e2, e3):
    if (e1[0] - e2[0]) != 0:
        x1 = (e1[1] - e2[1]) / (e1[0] - e2[0])
        y1 = e1[0] * x1 + e1[1]
    else:
        return True
    if (e2[0] - e3[0]) != 0:
        x2 = (e2[1] - e3[1]) / (e2[0] - e3[0])
        y2 = e2[0] * x2 + e2[1]
    else:
        return True
    return (x1 == x2) and (y1 == y2)


def checkparallel(m1, m2, m3):
    return (m1 == m2) or (m2 == m3) or (m1 == m3)


for _ in range(int(input())):
    N, C, K = map(int, input().split())
    A = []
    D = {}
    EQ = {}
    for i in range(N):
        a, b, c = map(int, input().split())
        if c not in D:
            D[c] = []
        D[c].append((a, b, c))
        EQ[(a, b, c)] = 0
    V = list(map(int, input().split()))
    V.insert(0, 0)
    nextflag = 1
    while K >= 0 and nextflag == 1:
        nextflag = 0
        ans = 0
        for col in D:
            if len(D[col]) >= 3:
                triangles = list(combinations(D[col], 3))
                triangles = list(set(triangles))
                for tri in triangles:
                    boolp = checkparallel(tri[0][0], tri[1][0], tri[2][0])
                    booli = checkintersection(tri[0], tri[1], tri[2])
                    if boolp == False and booli == False:  # Triangle
                        EQ[tri[0]] += 1
                        EQ[tri[1]] += 1
                        EQ[tri[2]] += 1
                        ans += 1
        EQ = {k: v for k, v in sorted(EQ.items(), key=lambda item: item[1], reverse=True)}
        for i in EQ:
            e = i
            if V[e[2]] <= K:
                K -= V[e[2]]
                nextflag = 1
                D[e[2]].remove(e)
                del EQ[i]
                break
    print(ans)
