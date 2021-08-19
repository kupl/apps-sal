class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        K -= 1
        (start, end) = (0, len(points) - 1)
        while start <= end:
            mid = self.__partition(points, start, end)
            if mid == K:
                break
            elif mid < K:
                start = mid + 1
            else:
                end = mid - 1
        return points[:K + 1]

    def __partition(self, points, lo, hi):

        def __dist(points, i):
            return points[i][0] ** 2 + points[i][1] ** 2
        d = __dist(points, lo)
        (i, j) = (lo, hi + 1)
        while True:
            while i < hi and __dist(points, i + 1) < d:
                i += 1
            while j > lo and __dist(points, j - 1) > d:
                j -= 1
            (i, j) = (i + 1, j - 1)
            if i >= j:
                break
            (points[i], points[j]) = (points[j], points[i])
        (points[lo], points[j]) = (points[j], points[lo])
        return j
