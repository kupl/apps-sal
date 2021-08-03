class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        self.quickselect(points, K, 0, len(points) - 1)
        return points[:K]

    def quickselect(self, points, k, lo, high):
        if lo >= high:
            return

        pivot = self.partition(points, lo, high)

        if pivot + 1 == k:
            return
        elif pivot < k:
            self.quickselect(points, k, pivot + 1, high)
        else:
            self.quickselect(points, k, lo, pivot - 1)

    def partition(self, points, lo, high):
        pivot = self.dist(points[high])
        w = lo

        for r in range(lo, high):
            if self.dist(points[r]) < pivot:
                points[w], points[r] = points[r], points[w]
                w += 1

        points[w], points[high] = points[high], points[w]
        return w

    def dist(self, pt):
        return pt[0]**2 + pt[1]**2
