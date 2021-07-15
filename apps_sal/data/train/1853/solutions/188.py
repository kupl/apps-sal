'''
Using Floyd-Warshall Algorithm
Reference: https://www.youtube.com/watch?v=oNI0rf2P9gE

TC: O(V^3)
SC: O(V^2)
'''
import heapq
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')]*n for _ in range(n)]
        graph = defaultdict(list)
        for u, v, w in edges:
            #graph[u].append((w,v))
            #graph[v].append((w,u))
            dist[u][v] = w
            dist[v][u] = w
            dist[u][u] = 0
            dist[v][v]
        
        minCities = n
        ans = -1
        
        '''
        Considering all paths between i, j going through each k vertex
        '''
        for k in range(n):
            for i in range(n):
                numCities = 0
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                    
                    if k == n-1:
                        if dist[i][j] <= distanceThreshold:
                            numCities += 1
                
                if k == n-1:
                    if numCities <= minCities:
                        ans = i
                        minCities = numCities
        
        return ans
                    

