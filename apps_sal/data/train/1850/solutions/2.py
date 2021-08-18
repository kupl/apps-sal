from collections import defaultdict


class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        dd = defaultdict(set)
        for u, v in edges:
            dd[u].add(v)
            dd[v].add(u)
        counts = [1] * N
        dists = [0] * N

        def dfs1(root, pre):
            for node in dd[root]:
                if node != pre:
                    dfs1(node, root)
                    counts[root] += counts[node]
                    dists[root] += dists[node] + counts[node]

        def dfs2(root, pre):
            for node in dd[root]:
                if node != pre:
                    dists[node] = dists[root] - 1 * counts[node] + 1 * (N - counts[node])
                    dfs2(node, root)
        dfs1(0, -1)
        dfs2(0, -1)
        return dists
