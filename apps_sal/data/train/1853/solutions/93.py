class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[float('inf') for _ in range(n)] for _ in range(n)]
        for v1, v2, w in edges:
            graph[v1][v2] = w
            graph[v2][v1] = w
        for i in range(n):
            graph[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        
        print(graph)
        
        currmin = float('inf')
        currv = -1
        for i in range(n):
            curr = 0
            for j in range(n):
                if graph[i][j] <= distanceThreshold:
                    curr += 1
                    if curr > currmin:
                        break
            if curr <= currmin:
                # print(i, curr)
                currmin = curr
                currv = i
        return currv
                    
        
                
                
            

