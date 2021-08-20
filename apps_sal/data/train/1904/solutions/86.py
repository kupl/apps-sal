class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        for i in range(len(points)):
            points[i].insert(0, (points[i][0] ** 2 + points[i][1] ** 2) ** 0.5)
        points.sort()
        ans = []
        for i in range(K):
            ans.append(points[i][1:])
        return ans
