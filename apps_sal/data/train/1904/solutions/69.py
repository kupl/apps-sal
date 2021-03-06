import heapq


def getDistance(point):
    return point[0] ** 2 + point[1] ** 2


class Solution:

    def swap(self, i, j):
        tmp = self.points_idx[i]
        tmp_dist = self.dist[i]
        self.points_idx[i] = self.points_idx[j]
        self.points_idx[j] = tmp
        self.dist[i] = self.dist[j]
        self.dist[j] = tmp_dist

    def partition(self, start, end, pivot):
        self.swap(0, pivot)
        left = 1
        right = end
        while left <= right:
            if self.dist[left] > self.dist[0]:
                self.swap(left, right)
                right -= 1
            else:
                left += 1
        self.swap(0, right)
        return right

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        n = len(points)
        if n <= K:
            return points
        self.points_idx = [i for i in range(n)]
        self.dist = []
        for i in range(n):
            self.dist.append(getDistance(points[i]))
        start = 0
        end = n - 1
        pivot = self.partition(0, n - 1, K)
        while pivot != K - 1:
            if pivot < K - 1:
                start = pivot + 1
            else:
                end = pivot - 1
            pivot = self.partition(start, end, start)
        res = [points[idx] for idx in self.points_idx[0:K]]
        return res
