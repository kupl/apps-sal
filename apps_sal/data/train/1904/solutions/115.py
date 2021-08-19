# use maxheap for nlogk

# Time - O(NlogN), Space - O(N)
# class Solution:
#     def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
#         points.sort(key = lambda points: points[0]**2 + points[1]**2)
#         return points[:K]

# Time - O(Nlogn), Space - O(N)
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
