import heapq


class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        point_map = {}
        for point in points:
            point_map[point[0], point[1]] = point[0] ** 2 + point[1] ** 2
        return [list(k) for (k, v) in sorted(point_map.items(), key=lambda kv: kv[1])[:K]]
