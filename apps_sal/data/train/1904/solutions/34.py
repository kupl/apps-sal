class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        from math import sqrt
        points.sort(key=lambda x: sqrt(x[0] ** 2 + x[1] ** 2))
        return points[:K]
