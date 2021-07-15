class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf1 = list(range(n+1))
        uf2 = list(range(n+1))
        def find(x, uf):
            if x != uf[x]:
                uf[x] = find(uf[x], uf)
            return uf[x]
        def union(x, y, uf):
            uf[find(x, uf)] = find(y, uf)
        edge_total = 0
        edge_1 = 0
        edge_2 = 0
       # make 1 first
        for w, v, u in sorted(edges, reverse=True):
            if w == 2:
                continue
            if find(v, uf1) == find(u, uf1):
                continue
            union(v, u, uf1)
            edge_1 += 1
            edge_total += 1
            if w == 3:
                union(v, u, uf2)
                edge_2 += 1
        if edge_1 < n-1:
            return -1
        # make 2 next
        for w, v, u in edges:
            if w == 1:
                continue
            if find(v, uf2) == find(u, uf2):
                continue
            union(v, u, uf2)
            edge_2 += 1
            if w == 2:
                edge_total += 1
        if edge_2 < n-1:
            return -1
        return len(edges) - edge_total
        

