import random


class Solution:
    def _value(self, point):
        return point[0] ** 2 + point[1] ** 2

    def _quickSelect(self, start: int, end: int, points: List[List[int]]) -> int:
        if start == end:
            return start
        p = random.randint(start, end)
        points[p], points[start] = points[start], points[p]
        j = start + 1
        for i in range(start + 1, end + 1):
            if self._value(points[i]) <= self._value(points[start]):
                points[i], points[j] = points[j], points[i]
                j += 1
        points[j - 1], points[start] = points[start], points[j - 1]
        return j - 1

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        start = 0
        end = len(points) - 1
        while True:
            p = self._quickSelect(start, end, points)
            if p < K - 1:
                start = p + 1
            elif p > K - 1:
                end = p - 1
            else:
                return points[:p + 1]
        return None
