class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        self.sort(0, len(points) - 1, points, K)
        return points[:K]

    def getDistance(self, a):
        return a[0] ** 2 + a[1] ** 2

    def sort(self, l, r, points, K):
        if l >= r:
            return
        mid = self.partition(l, r, points)
        if (mid - l + 1) < K:
            self.sort(mid + 1, r, points, K - (mid - l + 1))
        else:
            self.sort(l, mid - 1, points, K)

    def partition(self, i, j, points):
        pivot = self.getDistance(points[i])
        l = i
        r = j
        while True:
            while l <= r and self.getDistance(points[l]) <= pivot:
                l += 1
            while l <= r and self.getDistance(points[r]) > pivot:
                r -= 1
            if l >= r:
                break
            points[l], points[r] = points[r], points[l]
        points[i], points[r] = points[r], points[i]
        return r
