class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not points or len(points) < 1:
            return []
        distances = []
        
        for point in points:
            dist = point[0]*point[0] + point[1]*point[1]
            if len(distances) < K:
                heapq.heappush(distances, (-dist, point))
            else:
                if -dist > distances[0][0]:
                    heapq.heappushpop(distances, (-dist, point))
        
        return [point for _, point in distances]
