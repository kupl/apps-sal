from math import sqrt


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        sqrt_d = {}

        for x, y in points:
            sqrt_d[(x, y)] = sqrt(x**2 + y**2)

        # print(sqrt_d)
        return heapq.nsmallest(K, sqrt_d, key=lambda x: sqrt_d[x])
