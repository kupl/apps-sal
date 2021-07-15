class Solution:
    import math
    def distance(self, point):
        return math.sqrt(point[0]**2 + point[1]**2)
    
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distances = {}
        for point in points:
            distances[tuple(point)] = self.distance(point)
        print(distances)
        points_sorted = sorted(list(distances.keys()), key=lambda x: distances[x])
        
        return [list(i) for i in points_sorted[:K]]

