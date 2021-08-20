class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        (start, end) = (0, len(points) - 1)
        pivot = -1
        while start <= end:
            pivot = self.partition(points, start, end)
            if pivot == K:
                return points[0:pivot]
            elif pivot > K:
                end = pivot - 1
            else:
                start = pivot + 1
        return points

    def partition(self, points, start, end):
        pivot = start
        for i in range(start, end + 1):
            if self.dist(points, i) < self.dist(points, end):
                (points[i], points[pivot]) = (points[pivot], points[i])
                pivot += 1
        (points[end], points[pivot]) = (points[pivot], points[end])
        return pivot

    def dist(self, points, i):
        return points[i][0] ** 2 + points[i][1] ** 2
