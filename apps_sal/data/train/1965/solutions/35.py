class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        p = [-1 for i in range(n+1)]
        c = [1 for i in range(n+1)]

        def find(i, p, c):
            pi = p[i]
            nc = []
            nodes = []
            total = 0
            while pi != -1:
                nodes.append(i)
                nc.append(total)
                total = c[i]
                i = pi
                pi = p[i]
            for k, vi in enumerate(nodes):
                p[vi] = i
                c[vi] -= nc[k]
            return i

        def union(i, j, p, c):
            si, sj = find(i, p, c), find(j, p, c)
            if si == sj:
                return si
            if c[si] > c[sj]:
                p[sj] = si
                c[si] += c[sj]
                return si
            else:
                p[si] = sj
                c[sj] += c[si]
                return sj
            
        # connected component
        e1s = []
        e2s = []
        s = -1
        for i, ed in enumerate(edges):
            e, u, v = ed
            if e == 1:
                e1s.append(i)
            elif e == 2:
                e2s.append(i)
            else:
                ns = union(u, v, p, c)
                if s == -1 or c[s] < c[ns]:
                    s = ns
        pvst = set()
        num_edges = 0
        for i in range(1, n+1):
            si = find(i, p, c)
            if si in pvst:
                continue
            pvst.add(si)
            num_edges += c[si]-1
        
        def check(es):
            np = p.copy()
            nc = c.copy()
            for i in es:
                _, u, v = edges[i]
                union(u, v, np, nc)
            pset = {find(i, np, nc) for i in range(1, n+1)}
            return len(pset) == 1
        
        if not check(e1s) or not check(e2s):
            return -1
        need = 2*(n-1) - num_edges
        return len(edges) - need
