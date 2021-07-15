class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        #Floyd-Warshall
        
        dis = [[float(\"inf\") for _ in range(n)] for _ in range(n)]
        
        for edge in edges:
            dis[edge[0]][edge[1]] = dis[edge[1]][edge[0]] = edge[2]
        
        # note the outer loop index must be k
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k]+dis[k][j])
                    
        min_reach = float('inf')
        ans = n
        for i in range(n):
            reach = 0
            for j in range(n):
                if i != j and dis[i][j] <= distanceThreshold:
                    reach += 1
            
            if reach <= min_reach:
                ans = i
                min_reach = reach
 
        return ans
