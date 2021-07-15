class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        from heapq import heappush, heappop
        
        dis = [[float('inf')]*n for _ in range(n)]
        nei = collections.defaultdict(list)
        for i,j,x in edges:
            dis[i][j] = dis[j][i] = x
            nei[i].append(j)
            nei[j].append(i)
        for i in range(n):
            dis[i][i] = 0
        
        # Dijkstra
        visited = set()
        for i in range(n):
            pool = [(0,i)]                                          # pool[j] = x:  d(i,j) = x    
            while pool:
                x,j = heappop(pool)                                 # x = d(i,j)
                if (i,j) not in visited and x <= distanceThreshold: # early stop, if distance exceeds threshold
                    visited.add((i,j))
                    for k in nei[j]:
                        dis[i][k] = min(dis[i][k], dis[i][j]+dis[j][k])     # dis(i,k) = min(dis(i,k), dis(i,j)+dis(j,k))
                        heappush(pool, (dis[i][k], k))
        globalMin = [-1, -1]
        for i in range(n):
            total = 0
            for j in range(n):
                if dis[i][j] <= distanceThreshold:
                    total += 1
            if globalMin[0] == -1 or total <= globalMin[0]:
                globalMin[0] = total
                globalMin[1] = i
        return globalMin[1]

