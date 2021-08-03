class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distances = []

        for idx, point in enumerate(points):
            eucliDist = point[0]**2 + point[1]**2
            heapq.heappush(distances, (eucliDist, point))

        distances = heapq.nsmallest(K, distances)
        result = []
        for res in distances:
            result.append(res[1])

        return result
