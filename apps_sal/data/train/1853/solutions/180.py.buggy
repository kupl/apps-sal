from collections import defaultdict
class Solution:
    
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        g = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            g[i][i] = 0
        for e in edges:
            g[e[0]][e[1]] = e[2]
            g[e[1]][e[0]] = e[2]
       
\t   # Floyd Warshall's shortest path
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if g[i][j] > g[i][k] + g[k][j]:
                        g[i][j] = g[i][k] + g[k][j]
        res_node, res_connected = -1, math.inf
        for i in range(n):
            conn = 0
            for j in range(n):
                if g[i][j] <= distanceThreshold:
                    conn += 1
            if conn <= res_connected:
                res_node, res_connected = i, conn
        return res_node
            
        
