import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if K >= len(points):
            return points

        heap = []

        for i in range(K):
            distance = -1 * self.getDistance(points[i])
            heapq.heappush(heap, (distance, i))

        for i in range(K, len(points)):
            distance = -1 * self.getDistance(points[i])
            if distance > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (distance, i))

        result = []
        for p in heap:
            result.append(points[p[1]])

        return result

    def getDistance(self, point):
        return point[0]**2 + point[1]**2
