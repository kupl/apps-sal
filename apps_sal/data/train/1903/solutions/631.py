class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
    #没有现成的edge list，想到当遍历到某一个点才现算它与其他点的权重值并压进pqueue，故考虑首选Prim算法而不是Krusal
    # N = len(points)
    # dsu = list(range(N))
    # def find(i):
    #     if dsu[i] != i: dsu[i] = find(dsu[i])
    #     return dsu[i]
    # def union(i, j):
    #     dsu[find(j)] = find(i)
    
        N = len(points)
        seen = set()
        cost = 0
        cnt = 0
        pq = [(0, 0)]
        while pq:
            c, i = heapq.heappop(pq)
            if i in seen: continue
            cost += c
            cnt += 1
            if cnt == N: return cost
            seen.add(i)
            pt_x, pt_y = points[i]
            for j in range(N):
                if j in seen: continue
                nei_x, nei_y = points[j]
                nei_c = abs(pt_x - nei_x) + abs(pt_y - nei_y)
                heapq.heappush(pq, (nei_c, j))
        return cost
        
        
        
        
        
        
        
        
        
        
        
        
#         res = 0
#         N = len(points)
#         visited = [[0] * N for _ in range(N)]
#         if len(points) == 1: return 0
#         DP = [[float('inf')] * N for _ in range(N)]
        
#         for i in range(N):
#             # min_dist = float('inf')
#             for j in range(i+1, N):
#                 # print(i, i, j)
#                 x, y = points[i], points[j]
#                 curr_dist = DP[i][j] = DP[j][i] = abs(x[0] - y[0]) + abs(x[1] - y[1])
#                 # if curr_dist < min_dist: 
#                 #     min_dist = curr_dist
#             min_dist = min(DP[i])
#             j = DP[i].index(min_dist) 
#             if not visited[i][j]:
#                 res += min_dist
#                 visited[i][j] = visited[j][i] = 1
#                 DP[i][j] = DP[j][i] = float('inf')
#             print(min_dist, DP)
#             # res += min_dist
#         return res
                

