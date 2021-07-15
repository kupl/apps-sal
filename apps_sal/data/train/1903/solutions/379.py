class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        manhattan = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        n, c = len(points), collections.defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                d = manhattan(points[i], points[j])
                c[i].append((d, j))
                c[j].append((d, i))
        cnt, ans, visited, heap = 1, 0, [0] * n, c[0]
        visited[0] = 1
        heapq.heapify(heap)
    
        while heap:
            d, j = heapq.heappop(heap)
            if not visited[j]:
                visited[j], cnt, ans = 1, cnt+1, ans+d
                for record in c[j]: heapq.heappush(heap, record)
            if cnt >= n: break        
        return ans
        
#         if not points or len(points) <= 1:
#             return 0
        
#         heap = []
#         for i in range(len(points)):
#             for j in range(i + 1, len(points)):
#                 p1 = points[i]
#                 p2 = points[j]
#                 dis = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
#                 heapq.heappush(heap, (dis, i, j))
        
#         self.father = [i for i in range(len(points))]
#         res = 0
#         while heap:
#             dis, u, v = heapq.heappop(heap)
#             root_u = self.find(u)
#             root_v = self.find(v)
#             if root_u == root_v:
#                 continue
#             self.father[max(root_u, root_v)] = min(root_u, root_v)
#             res += dis
        
#         return res
    
#     def find(self, x):
#         if self.father[x] == x:
#             return self.father[x]
#         self.father[x] = self.find(self.father[x])
#         return self.father[x]

