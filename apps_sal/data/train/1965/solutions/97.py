class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def find(p, x):
            if p[x] != x:
                p[x] = find(p, p[x])
            return p[x]

        def merge(p, x, y):
            x = p[x]
            y = p[y]
            if x < y:
                p[y] = x
            else:
                p[x] = y
        parent = [x for x in range(n + 1)]
        path = 0
        for e in edges:
            if e[0] == 3 and find(parent, e[1]) != find(parent, e[2]):
                merge(parent, e[1], e[2])
                path += 1
        a, b = list(parent), list(parent)
        patha, pathb = 0, 0
        for e in edges:
            if e[0] == 1 and find(a, e[1]) != find(a, e[2]):
                merge(a, e[1], e[2])
                patha += 1
            if e[0] == 2 and find(b, e[1]) != find(b, e[2]):
                merge(b, e[1], e[2])
                pathb += 1
        if patha + path != n - 1 or pathb + path != n - 1:
            return -1
        return len(edges) - (path + patha + pathb)
