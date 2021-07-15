class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prims algorithm O(V+ElogV)
        if not points or len(points) <= 1:
            return 0
        
        p_dis = {}
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1 = points[i]
                p2 = points[j]
                dis = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                p_dis.setdefault(i, [])
                p_dis.setdefault(j, [])
                p_dis[i].append((dis, j))
                p_dis[j].append((dis, i))
        
        visited = [False] * len(points)
        visited[0] = True
        count = 1
        heap = []
        res = 0
        for d, p in p_dis[0]:
            heapq.heappush(heap, (d, p))
        while heap:
            dis, p = heapq.heappop(heap)
            if not visited[p]:
                count += 1
                visited[p] = True
                res += dis
                for _d, _p in p_dis[p]:
                    heapq.heappush(heap, (_d, _p))
            
            if count == len(points):
                break
        
        return res
        
        
        
        # Kruskal algorithm
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

