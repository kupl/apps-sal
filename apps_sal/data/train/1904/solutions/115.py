

import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        ans = []
        min_heap = []
        for pnt in points:
            heapq.heappush(min_heap, (pnt[0]**2 + pnt[1]**2, pnt))
        for i in range(K):
            ans.append(heapq.heappop(min_heap)[1])

        return ans
