class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n + 1)]
        wei = [1 for i in range(n + 1)]

        def find(i, p):
            if p[i] != p[p[i]]:
                p[i] = find(p[i], p)
            return p[i]

        def united(i, j, p):
            return find(i, p) == find(j, p)

        def unite(i, j, p, w):
            zi = find(i, p)
            zj = find(j, p)
            if w[zi] > w[zj]:
                p[zj] = zi
                w[zi] = w[zi] + w[zj]
                w[zj] = 0
            else:
                p[zi] = zj
                w[zj] = w[zi] + w[zj]
                w[zi] = 0
        edges.sort()
        ans = 0
        for (t, a, b) in reversed(edges):
            if t != 3:
                break
            if united(a, b, par):
                ans += 1
            else:
                unite(a, b, par, wei)
        p = [None, par[:], par[:]]
        w = [None, wei[:], wei[:]]
        for (t, a, b) in edges:
            if t > 2:
                break
            if united(a, b, p[t]):
                ans += 1
            else:
                unite(a, b, p[t], w[t])
        for i in range(2, n + 1):
            if not united(1, i, p[1]):
                return -1
            if not united(1, i, p[2]):
                return -1
        return ans
