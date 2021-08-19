import random


class Solution:
    # def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    #     values = [(points[i][0] ** 2 + points[i][1] ** 2, i) for i in range(len(points))]
    #     values.sort()
    #     return [points[i] for _, i in values[:K]]
    def _value(self, point):
        return point[0] ** 2 + point[1] ** 2

    def _quickSelect(self, start: int, end: int, points: List[List[int]]) -> int:
        if start == end:
            return start
        # random pivot
        p = random.randint(start, end)
        points[p], points[start] = points[start], points[p]
        j = start + 1
        for i in range(start + 1, end + 1):
            if self._value(points[i]) <= self._value(points[start]):
                points[i], points[j] = points[j], points[i]
                j += 1
        # swap i to its correct position
        points[j - 1], points[start] = points[start], points[j - 1]
        return j - 1

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        start = 0
        end = len(points) - 1
        # select the pivot using quick select
        while True:
            p = self._quickSelect(start, end, points)
            # if the pivot <= K: quick select for K on the right
            # print(p)
            if p < K - 1:
                start = p + 1
            elif p > K - 1:
                end = p - 1
            else:
                return points[:p + 1]
        return None
