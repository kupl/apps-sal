from collections import defaultdict
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        adj = defaultdict(set)
        for u,v in dislikes:
            adj[u].add(v)
            adj[v].add(u)
        color = [-1] * (N + 1)
        for i in range(1,N+1):
            if color[i] == -1:
                color[i] = 0
                Q = [i]
                while Q:
                    new = []
                    for cur in Q:
                        for nxt in adj[cur]:
                            if color[nxt] == color[cur]:
                                return False
                            if color[nxt] == -1:
                                color[nxt] = 1- color[cur]
                                new.append(nxt)
                    Q = new
        return True
