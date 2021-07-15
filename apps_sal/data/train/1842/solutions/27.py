class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        neighbors = defaultdict(list)
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
        
        def dfs(u, tt, r):
            if tt > t or u in visited:
                return 0
            if u == target:
                if len(neighbors[u]) > (0 if r else 1) and tt < t:
                    return 0
                else:
                    return 1
            visited.add(u)
            m = 0
            for v in neighbors[u]:
                m = max(m, dfs(v, tt+1, False))
            visited.remove(u)
            if r and neighbors[u]:
                return m / len(neighbors[u])
            elif not r and len(neighbors[u]) > 1:
                return m / (len(neighbors[u]) - 1)
            else:
                return 0
        
        visited = set()
        return dfs(1, 0, True)
            

