class Solution:
    def kClosest(self, points, K: int):

        return [points[i] for d, i in sorted([[x[0]**2 + x[1]**2, i] for i, x in enumerate(points)])[0:K]]
