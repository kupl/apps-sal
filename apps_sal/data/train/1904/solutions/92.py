class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        output = []

        for i in range(len(points)):
            distance = (points[i][0]**2) + (points[i][1]**2)
            heapq.heappush(heap, (distance, points[i]))

        for i in range(K):
            add = (heapq.heappop(heap))
            output.append(add[1])

        return output
