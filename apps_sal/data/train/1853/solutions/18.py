from collections import defaultdict

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        cityGraph = [[float(\"inf\") for col in range(n)] for row in range(n)]
        for edge in edges:
            cityGraph[edge[0]][edge[1]] = edge[2]
            cityGraph[edge[1]][edge[0]] = edge[2]
            
        
        for intermediateCity in range(n):
            for startCity in range(n):
                for endCity in range(n):
                    if startCity != endCity:
                        cityGraph[startCity][endCity] = min(cityGraph[startCity][endCity], cityGraph[startCity][intermediateCity]+cityGraph[intermediateCity][endCity])
        
        cityThresholdSum = [sum(1 for cityDist in city if cityDist <= distanceThreshold) for city in cityGraph]
        
        return len(cityThresholdSum) - 1 -cityThresholdSum[::-1].index(min(cityThresholdSum))
