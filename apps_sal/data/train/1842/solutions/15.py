class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        #         if n == 1: return 1.0
        #         G = [[] for i in range(n + 1)]
        #         for i, j in edges:
        #             G[i].append(j)
        #             G[j].append(i)
        #         seen = [0] * (n + 1)

        #         def dfs(i, t):
        #             if i != 1 and len(G[i]) == 1 or t == 0:
        #                 return i == target
        #             seen[i] = 1
        #             res = sum(dfs(j, t - 1) for j in G[i] if not seen[j])
        #             return res * 1.0 / (len(G[i]) - (i != 1))
        #         return dfs(1, t)

        nei = collections.defaultdict(set)
        for a, b in edges:
            nei[a].add(b)
            nei[b].add(a)

        visited, res = set(), 0.

        def dfs(leaf_id, p, time):
            nonlocal res
            if time >= t:
                if leaf_id == target:
                    res = p
                return
            visited.add(leaf_id)
            neighbors = nei[leaf_id] - visited
            for n in neighbors or [leaf_id]:
                dfs(n, p / (len(neighbors) or 1), time + 1)
        dfs(1, 1, 0)
        return res
