from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def solve():
    INF = float('inf')

    N, Q = list(map(int, input().split()))
    adjL = [[] for _ in range(N)]
    for _ in range(N - 1):
        A, B, C, D = list(map(int, input().split()))
        A, B, C = A - 1, B - 1, C - 1
        adjL[A].append((B, C, D))
        adjL[B].append((A, C, D))
    querys = [tuple(map(int, input().split())) for _ in range(Q)]

    def dfs(vNow, vPar, depth):
        iVFirsts[vNow] = len(vs)
        vs.append(vNow)
        depths.append(depth)
        for v2, clr, dist in adjL[vNow]:
            if v2 == vPar:
                continue
            iVColorss[clr].append(len(numEs))
            numEs.append(1)
            sumDs.append(dist)

            dfs(v2, vNow, depth + 1)

            vs.append(vNow)
            depths.append(depth)
            iVColorss[clr].append(len(numEs))
            numEs.append(-1)
            sumDs.append(-dist)

    vs = []
    iVFirsts = [-1] * N
    depths = []
    numEs = [0]
    sumDs = [0]
    iVColorss = [[0] for _ in range(N - 1)]

    dfs(0, -1, 0)

    dists = [0] * N
    accD = 0
    for i, sumD in enumerate(sumDs):
        accD += sumD
        if iVFirsts[vs[i]] == i:
            dists[vs[i]] = accD

    for iVColors in iVColorss:
        for i in range(1, len(iVColors)):
            numEs[iVColors[i]] += numEs[iVColors[i - 1]]
            sumDs[iVColors[i]] += sumDs[iVColors[i - 1]]

    idEle = (INF, -1)

    def _binOpe(x, y):
        return x if x <= y else y

    def makeSegTree(numEle):
        numPow2 = 2 ** (numEle - 1).bit_length()
        data = [idEle] * (2 * numPow2)
        return data, numPow2

    def setInit(As):
        for iST, A in enumerate(As, numPow2):
            data[iST] = A
        for iST in reversed(list(range(1, numPow2))):
            data[iST] = _binOpe(data[2 * iST], data[2 * iST + 1])

    def getValue(iSt, iEn):
        L = iSt + numPow2
        R = iEn + numPow2
        ans = idEle
        while L < R:
            if L & 1:
                ans = _binOpe(ans, data[L])
                L += 1
            if R & 1:
                R -= 1
                ans = _binOpe(ans, data[R])
            L >>= 1
            R >>= 1
        return ans

    data, numPow2 = makeSegTree(len(depths))
    setInit([(depth, i) for i, depth in enumerate(depths)])

    def getLCA(x, y):
        L, R = iVFirsts[x], iVFirsts[y]
        if L > R:
            L, R = R, L
        minV, iMinV = getValue(L, R)
        return vs[iMinV]

    anss = []
    for clr, distNew, u, v in querys:
        u, v = u - 1, v - 1
        LCA = getLCA(u, v)

        clr -= 1
        ds = [dists[u], dists[v], dists[LCA]]
        for i, vv in enumerate([u, v, LCA]):
            iIV = bisect_right(iVColorss[clr], iVFirsts[vv]) - 1
            iV = iVColorss[clr][iIV]
            ds[i] += numEs[iV] * distNew - sumDs[iV]
        ans = ds[0] + ds[1] - 2 * ds[2]
        anss.append(ans)

    print(('\n'.join(map(str, anss))))


solve()
