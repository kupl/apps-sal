import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dis(s, e):
            return abs(s[0] - e[0]) + abs(s[1] - e[1])
        
        def find(u):
            if root[u] != u:
                root[u] = find(root[u])
            return root[u]
        
        def union(u, v):
            ru, rv = find(u), find(v)
            if ru == rv:
                return False
            if rank[ru] < rank[rv]:
                root[ru] = rv
                rank[rv] = rank[ru] + rank[rv]
            else:
                root[rv] = ru
                rank[ru] = rank[ru] + rank[rv]
            return True
        
        n = len(points)
        res = 0
        queue = []
        root = [i for i in range(n)]
        rank = [1] * n
        for i in range(n):
            s = points[i]
            for j in range(i+1, n):
                e = points[j]
                heapq.heappush(queue, (dis(s, e), i, j))
        while queue:
            dis, s, e = heapq.heappop(queue)
            if union(s, e):
                res += dis
        return res

