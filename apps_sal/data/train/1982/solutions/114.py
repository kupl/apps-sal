class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        g = collections.defaultdict(list)
        for (u, v) in dislikes:
            g[u].append(v)
            g[v].append(u)
        parent = [i for i in range(N + 1)]

        def find(n):
            if n == parent[n]:
                return n
            parent[n] = find(parent[n])
            return parent[n]

        def union(n1, n2):
            (r1, r2) = (find(n1), find(n2))
            if r1 != r2:
                parent[r1] = r2
        for k in g:
            for node in g[k]:
                if find(k) == find(node):
                    return False
                union(g[k][0], node)
        return True
