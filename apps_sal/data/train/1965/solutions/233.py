class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:     
        graph = {1: [], 2: [], 3: []}
        for t, i, j in edges:
            graph[t].append((i, j))
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            if rank[px] < rank[py]:
                px, py = py, px
            parents[py] = px
            rank[px] += rank[px] == rank[py]
            return True
        
        result = 0
        parents = list(range(n + 1))
        rank = [1] * (n + 1)
        for i, j in graph[3]:
            if not union(i, j):
                result += 1
        parents_copy = parents[:]
        rank_copy = rank[:]
        for i, j in graph[1]:
            if not union(i, j):
                result += 1
        if len(set(find(i) for i in range(1, n + 1))) > 1:
            return -1
        parents = parents_copy
        rank = rank_copy
        for i, j in graph[2]:
            if not union(i, j):
                result += 1
        if len(set(find(i) for i in range(1, n + 1))) > 1:
            return -1
        return result

