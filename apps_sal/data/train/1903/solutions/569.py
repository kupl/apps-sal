class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # MST search algorithm Prim
        G = collections.defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dis = abs(points[i][0]-points[j][0]) + abs(points[i][1] - points[j][1])
                G[i].append((dis, j))
                G[j].append((dis, i))
        # print(G)
        visited = {0}
        pq = G[0]
        heapq.heapify(pq)
        res = 0
        while len(visited) < len(points) and pq:
            w, v = heapq.heappop(pq)
            if v not in visited:
                res += w
                visited.add(v)
                for w, nei in G[v]:
                    if nei not in visited:
                        heapq.heappush(pq, (w,nei))
        return res
        
        
        
        # MST search algorithm Kruskal
        # create MST over a created graph
#         q = []
#         for i in range(len(points)):
#             for j in range(i+1, len(points)):
#                 dis = abs(points[i][0]-points[j][0]) + abs(points[i][1] - points[j][1])
#                 q.append((dis, i, j))
        
#         def find(x):
#             if (x != parent[x]):
#                 parent[x] = find(parent[x])
#             return parent[x]
#         def union(x, y):
#             if size[x] > size[y]:
#                 size[x] += size[y]
#                 parent[y] = x
#             else:
#                 size[y] += size[x]
#                 parent[x] = y
                
#         n = len(points)
#         parent = [i for i in range(n+1)]
#         size = [1 for _ in range(n+1)]  
#         q.sort()  # sort edges
#         res = 0
#         count = 0
#         for w, u, v in q:
#             rA, rB = find(u), find(v)
#             if rA == rB:
#                 continue
#             union(rA, rB)
#             res += w
#             # Optimize so that we don't traverse all edges
#             count += 1
#             if count == n:
#                 return res
#         return res 

