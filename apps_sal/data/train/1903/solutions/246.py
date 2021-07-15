class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ans = 0
        current_point_index = 0
        visited_point_indeces = set()
        distance_list = [float('inf')] * len(points)
        
        for i in range(len(points) - 1):
            visited_point_indeces.add(current_point_index)
            
            for j in range(len(points)):
                if j in visited_point_indeces: continue
                    
                x, y = points[current_point_index]
                x0, y0 = points[j]
                
                distance_list[j] = min(distance_list[j], abs(y0 - y) + abs(x0 - x))
                
            distance_list[current_point_index] = float('inf')
            delta, current_point_index = min([distance, index] for index, distance in enumerate(distance_list))
            ans += delta
            
        return ans

