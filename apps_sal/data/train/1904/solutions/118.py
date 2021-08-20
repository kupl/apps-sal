class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda point: point[0] * point[0] + point[1] * point[1])
        return points[:K]
