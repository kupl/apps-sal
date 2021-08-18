import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def distance(point):
            return (point[0] ** 2 + point[1] ** 2)

        return sorted(points, key=distance)[:K]
