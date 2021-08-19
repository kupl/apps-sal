class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def distance(point):
            x, y = point
            return x ** 2 + y ** 2

        # negative values to make a min-heap a max-heap
        distances = [(distance(p), p) for p in points]
        heapq.heapify(distances)

        for point in points:
            heapq.heappushpop(distances, (-distance(point), point))
        return [p for _, p in heapq.nsmallest(K, distances)]
