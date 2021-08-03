import math


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        distances = {}

        d = []

#         large = -float(inf)
#         small = float(inf)

        for i in range(len(points)):

            dist = math.sqrt(points[i][0] ** 2 + points[i][1] ** 2)
            # print(dist)
            distances[dist] = distances.get(dist, []) + [points[i]]
            d.append(dist)

        # print(distances)
        d.sort()
        ans = []

        for i in range(K):
            if i != 0 and d[i] == d[i - 1]:
                continue
            ans = ans + distances[d[i]]

        return ans
