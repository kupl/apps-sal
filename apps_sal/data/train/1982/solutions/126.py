class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        def dfs(p1, color=1):
            colors[color].add(p1)
            for p2 in G[p1]:
                if p2 in colors[color] or (p2 not in colors[-color] and not dfs(p2, -color)):
                    return False
            return True
        G, colors = [[] for _ in range(N)], {-1: set(), 1: set()}
        for p1, p2 in dislikes:
            G[p1-1].append(p2-1)
            G[p2-1].append(p1-1)
        for p in range(N):
            if p not in colors[1] and p not in colors[-1] and not dfs(p):
                return False
        return True
