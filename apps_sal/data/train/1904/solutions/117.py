import heapq


class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        def get_distance(points):
            return sqrt(points[0] ** 2 + points[1] ** 2)
        dist = [[get_distance(point), point] for point in points]
        heapq.heapify(dist)
        ans = []
        for i in range(K):
            ans.append(heapq.heappop(dist)[1])
        return ans
