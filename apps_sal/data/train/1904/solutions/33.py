class Solution:

    def _getDistance(self, point):
        dis = math.sqrt(point[0] ** 2 + point[1] ** 2)
        return dis

    def _partition(self, start, end, points):
        target = points[start]
        while start < end:
            while start < end and self._getDistance(points[end]) >= self._getDistance(target):
                end -= 1
            points[start] = points[end]
            while start < end and self._getDistance(points[start]) <= self._getDistance(target):
                start += 1
            points[end] = points[start]
        points[start] = target
        return start

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not points:
            return []
        start = 0
        end = len(points) - 1
        while start <= end:
            mid = self._partition(start, end, points)
            if mid == K:
                return points[:K]
            elif mid > K:
                end = mid - 1
            else:
                start = mid + 1
        return points[:K]
