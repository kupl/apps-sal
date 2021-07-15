class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        pointDistances = [
            [point, self.calculateDistanceToOrigin(point)]
            for point in points
        ]
        
        sortedPoints = sorted(pointDistances, key=lambda pd: pd[1])
        return [pd[0] for pd in sortedPoints[:K]]
                
    
    def calculateDistanceToOrigin(self, point):
        return point[0] * point[0] + point[1] * point[1] 
