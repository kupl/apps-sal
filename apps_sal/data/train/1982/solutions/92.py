class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        colors = [''] * N
        edges = [[] for _ in range(N)]
        for p1, p2 in dislikes:
            edges[p1-1].append(p2-1)
            edges[p2-1].append(p1-1)

        def dfs(i, d):
            colors[i] = 'r' if d == 0 else 'b'
            for p in edges[i]:
                if colors[p] != '':
                    if colors[p] == 'r' and d == 0: return False
                    if colors[p] == 'b' and d == 1: return False
                elif not dfs(p, (d+1)%2): return False
            return True
        for i in range(N):
            if colors[i] == '':
                if not dfs(i, 0):
                    return False
        return True
