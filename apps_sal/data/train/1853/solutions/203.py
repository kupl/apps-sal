'''
Using Dijkstra's Algorithm

Idea:
1) Do Dijkstra from every node due to the weights are non-negative
2) For each city calculate the number of reachable cities within the threshold, then search for the optimal city.

'''
import heapq
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((w,v))
            graph[v].append((w,u))
        
        dist = [[float('inf')]*n for _ in range(n)]
        minCities = n
        ans = -1
        
        for i in range(n):
            q = [(0,i)]
            validCities = 0
            
            while q:
                #print(q)
                distance, node = heapq.heappop(q)
                if distance < dist[i][node]:
                    dist[i][node] = distance
                    if distance <= distanceThreshold:
                        validCities += 1
                else:
                    continue
                
                for neigh in graph[node]:
                    if distance + neigh[0] < dist[i][neigh[1]]:
                        heapq.heappush(q, (distance + neigh[0], neigh[1]))
            
            if validCities <= minCities:
                minCities = validCities
                ans = i
            
        #print(dist)
        #print(ans)
        return ans
