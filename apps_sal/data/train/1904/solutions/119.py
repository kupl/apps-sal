from heapq import *


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        hp = []
        n = len(points)
        if K >= n:
            return points
        if K == 0:
            return []
        for x, y in points:
            key = -(x**(2) + y**(2))
            if len(hp) < K:
                heappush(hp, (key, x, y))
            else:
                if -hp[0][0] > -key:
                    heappop(hp)
                    heappush(hp, (key, x, y))
        ans = []
        for _ in range(K):
            key, x, y = heappop(hp)
            ans.append([x, y])
        return ans
