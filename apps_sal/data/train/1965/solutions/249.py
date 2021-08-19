from collections import defaultdict


class Solution:

    def maxNumEdgesToRemove(self, n, edges) -> int:
        e = [defaultdict(lambda: set()) for i in range(3)]
        d = 0
        for edge in edges:
            (t, x, y) = edge
            x -= 1
            y -= 1
            t -= 1
            if y in e[t][x]:
                d += 1
            else:
                e[t][x].add(y)
                e[t][y].add(x)
        q = 0
        for i in range(n):
            for j in e[2][i]:
                for k in range(2):
                    if j in e[k][i]:
                        q += 1
                        e[k][i].remove(j)
        q = q >> 1

        def visit(v, c, t, o):
            v[c] = o
            for i in e[t][c]:
                if v[i] == -1:
                    visit(v, i, t, o)
            if t != 2:
                for i in e[2][c]:
                    if v[i] == -1:
                        visit(v, i, t, o)

        def solve(t):
            v = [-1] * n
            p = 0
            for i in range(n):
                if v[i] == -1:
                    visit(v, i, t, p)
                    p += 1
            mp = [0] * p
            cp = [0] * p
            for i in range(n):
                mp[v[i]] += len(e[t][i])
                cp[v[i]] += 1
            return (p, mp, cp, v)
        r = d + q
        (p2, mp2, cp2, vp2) = solve(2)
        for i in range(p2):
            r += (mp2[i] >> 1) - (cp2[i] - 1)
        rr = [solve(t) for t in range(2)]
        if rr[0][0] != 1 or rr[1][0] != 1:
            return -1
        tp = p2 + (n - sum(cp2))
        for k in range(2):
            ee = 0
            tt = 0
            for i in range(n):
                for j in e[k][i]:
                    if vp2[i] != vp2[j]:
                        ee += 1
                    else:
                        tt += 1
            ee = ee >> 1
            tt = tt >> 1
            r += ee - (tp - 1) + tt
        return r
