class Solution:
    def calculateEuclidean(self, point):
        return (point[0]) ** 2 + (point[1]) ** 2

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []

        for point in points:
            heapq.heappush(heap, (-self.calculateEuclidean(point), point))

            if len(heap) > K:
                heapq.heappop(heap)

        return [point[1] for point in heap]
