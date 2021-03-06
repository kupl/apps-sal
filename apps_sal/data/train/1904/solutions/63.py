class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        d = {}
        ans = []
        points = sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)
        for i in range(K):
            ans.append(points[i])
        return ans
