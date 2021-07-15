from queue import PriorityQueue
 class Solution(object):
     def pourWater(self, heights, V, K):
         """
         :type heights: List[int]
         :type V: int
         :type K: int
         :rtype: List[int]
         """
         i = 0
         while i < V:
             l_i = K-1
             at = K
             while l_i>=0 and heights[l_i] <= heights[at]:
                 if heights[l_i] < heights[at]:
                     at = l_i
                 l_i-=1
             if at != K:
                 heights[at] +=1
                 i+=1
                 continue
             r_i = K+1
             while r_i < len(heights) and heights[r_i] <= heights[at]:
                 if heights[r_i] < heights[at]:
                     at = r_i
                 r_i+=1
             if at != K:
                 heights[at] +=1
                 i+=1
                 continue
             heights[K] += 1
             i+=1
         return heights
             
             
                 
             
