import heapq
 class Solution(object):
     def pourWater(self, heights, V, K):
         """
         :type heights: List[int]
         :type V: int
         :type K: int
         :rtype: List[int]
         """
 
         heap = []
         heapq.heappush(heap, (heights[K], -1, 0))
         l, r = K - 1, K + 1
         lh, rh = [], []
 
         for i in range(V):
             while l >= 0 and heights[l] <= heights[l + 1]:
                 heapq.heappush(lh, (heights[l], -l))
                 l -= 1
 
             while r < len(heights) and heights[r] <= heights[r - 1]:
                 heapq.heappush(rh, (heights[r], r))
                 r += 1
 
             if lh and lh[0][0] < heights[K]:
                 h, i = heapq.heappop(lh)
                 heights[-i] += 1
                 heapq.heappush(lh, (h + 1, i))
                 continue
 
             if rh and rh[0][0] < heights[K]:
                 h, i = heapq.heappop(rh)
                 heights[i] += 1
                 heapq.heappush(rh, (h + 1, i))
                 continue
 
             heights[K] += 1
 
         return heights

