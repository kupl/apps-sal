
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1: 
            return 0

        result = 0 
        distance = [math.inf] * len(points)  # idx -> distance 
        current = 0
        combined = set() 

        for i in range(len(points)-1): 
            combined.add(current)
            x, y = points[current]
            for j in range(len(points)): 
                if j in combined:
                    continue
                x2, y2 = points[j]
                distance[j] = min(distance[j], abs(x-x2) + abs(y-y2))

            d = 0
            for j in range(len(distance)):
                if distance[j] < distance[current]:
                    current = j
                    d = distance[j]\t
            distance[current] = math.inf
            result += d

        return result 



