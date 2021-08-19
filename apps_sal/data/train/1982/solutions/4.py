class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        groups = [0] * (N + 1)
        adj = collections.defaultdict(list)
        for [i, j] in dislikes:
            adj[i].append(j)
            adj[j].append(i)

        def dfs(i):
            for nei in adj[i]:
                if groups[nei]:
                    if groups[nei] == groups[i]:
                        return False
                else:
                    groups[nei] = -groups[i]
                    if not dfs(nei):
                        return False
            return True
        for i in range(N):
            if not groups[i]:
                groups[i] = 1
                if not dfs(i):
                    return False
        return True
