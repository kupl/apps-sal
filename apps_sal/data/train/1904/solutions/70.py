from heapq import heappop, heappush, heapify


class Solution:

    def distFromOrigin(self, x, y):
        return sqrt(x ** 2 + y ** 2)

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = self.distFromOrigin(point[0], point[1])
            if len(heap) == K:
                if dist < -heap[0][0]:
                    heappop(heap)
                    heappush(heap, (-dist, point))
            else:
                heappush(heap, (-dist, point))
        output = []
        for item in heap:
            output.append(item[1])
        return output
