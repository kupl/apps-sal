class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        def manhantan_distance(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        
        n = len(points)
        included = {0}
        distances = [manhantan_distance(points[0], point) for point in points]
        cost = 0
        while len(included) < n:
            to_add = None
            cost_to_add = float('inf')
            for i, distance in enumerate(distances):
                if i in included:
                    continue
                if distance < cost_to_add:
                    to_add = i
                    cost_to_add = distance
            
            included.add(to_add)
            cost += cost_to_add
            
            new_point = points[to_add]
            for i, point in enumerate(points):
                new_distance = manhantan_distance(new_point, point)
                distances[i] = min(distances[i], new_distance)
            
        return cost

