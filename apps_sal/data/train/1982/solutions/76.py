class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if len(dislikes) == 0:
            return True
        colors = [None] * N
        G = {}
        for edge in dislikes:
            if edge[0] - 1 not in G:
                G[edge[0] - 1] = [edge[1] - 1]
            else:
                G[edge[0] - 1].append(edge[1] - 1)
            if edge[1] - 1 not in G:
                G[edge[1] - 1] = [edge[0] - 1]
            else:
                G[edge[1] - 1].append(edge[0] - 1)

        def dfs(node, clr):
            colors[node] = clr
            if node not in G:
                return True
            for adj in G[node]:
                if colors[adj] is None:
                    if not dfs(adj, not clr):
                        return False
                elif colors[adj] == clr:
                    return False
            return True
        for i in range(N):
            if colors[i] is None:
                if not dfs(i, True):
                    return False
        return True
