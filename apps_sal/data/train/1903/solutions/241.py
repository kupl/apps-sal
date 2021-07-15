# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         manhattan = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
#         n, c = len(points), collections.defaultdict(list)
#         for i in range(n):
#             for j in range(i+1, n):
#                 d = manhattan(points[i], points[j])
#                 c[i].append((d, j))
#                 c[j].append((d, i))
#         cnt, ans, visited, heap = 1, 0, [0] * n, c[0]
#         visited[0] = 1
#         heapq.heapify(heap)
#         while heap:
#             d, j = heapq.heappop(heap)
#             if not visited[j]:
#                 visited[j], cnt, ans = 1, cnt+1, ans+d
#                 for record in c[j]: heapq.heappush(heap, record)
#             if cnt >= n: break        
#         return ans

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
    
    # make a and b part of the same component
    # union by rank optimization
    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb: return
        if self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
            self.rank[pa] += self.rank[pb]
        else:
            self.parent[pa] = pb
            self.rank[pb] += self.rank[pa]
    
    # find the representative of the 
    # path compression optimization
    def find(self, a):
        if self.parent[a] == a:
            return a
        
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
    

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i+1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))
        
        # sort based on cost (i.e. distance)
        edges.sort()
        
        # using Kruskal's algorithm to find the cost of Minimum Spanning Tree
        res = 0
        ds = DisjointSet(n)
        cnt = 0
        for cost, u, v in edges:
            if ds.find(u) != ds.find(v):
                ds.union(u, v)
                res += cost
                cnt += 1
            if cnt == len(points) -1:
                break
        return res
