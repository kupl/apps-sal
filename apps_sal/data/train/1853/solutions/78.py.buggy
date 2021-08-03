class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        distance = [[float(\"inf\")] * n for i in range(n)]
        
        for city_1, city_2, weight in edges:
            
            distance[city_1][city_2] = weight
            distance[city_2][city_1] = weight
            
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    
                    if i == j:
                        continue
                    
                    distance[i][j] = min(distance[i][k] + distance[k][j], distance[i][j])
                    distance[j][i] = distance[i][j]
                            
        counts = []
        for i in range(n):
            
            within_threshold = 0
            for j in range(n):
                
                if distance[i][j] <= distanceThreshold:
                    within_threshold += 1
                    
            counts.append(within_threshold)
                        
        minimum_city_index = -1
        minimum_city_distance = float(\"inf\")
        for i in range(n):
            
            if counts[i] <= minimum_city_distance:
                
                minimum_city_index = i
                minimum_city_distance = counts[i]
                
        return minimum_city_index
            
            
