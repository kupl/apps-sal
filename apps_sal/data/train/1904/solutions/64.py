import math


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        a = []
        for i in range(len(points)):
            a.append([math.sqrt(pow(points[i][0], 2) + pow(points[i][1], 2)), [points[i][0], points[i][1]]])
        a.sort(key=lambda x: x[0])
        print(a)
        l = []
        for j in range(K):
            l.append(a[j][1])
        return l
