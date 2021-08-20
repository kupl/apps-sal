class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        def norm(point):
            return point[0] ** 2 + point[1] ** 2
        dis = []
        for point in points:
            dis.append(norm(point))
        (dis, points) = list(zip(*sorted(zip(dis, points))))
        res = []
        for i in range(K):
            res.append(points[i])
        return res
