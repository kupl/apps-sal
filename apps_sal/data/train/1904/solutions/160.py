class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        self.countK(points, 0, len(points) - 1, K)
        return points[:K]

    def countK(self, points, l, r, k):
        if l < r:
            p = self.createPartition(points, l, r, k)
            if p == k:
                return
            elif p < k:
                self.countK(points, p + 1, r, k)
            else:
                self.countK(points, l, p - 1, k)

    def createPartition(self, points, l, r, k):
        pivot = points[r]
        count = l
        for i in range(l, r):
            if (points[i][0]**2 + points[i][1]**2) <= (pivot[0]**2 + pivot[1]**2):
                points[i], points[count] = points[count], points[i]
                count += 1
        points[count], points[r] = points[r], points[count]
        return count
