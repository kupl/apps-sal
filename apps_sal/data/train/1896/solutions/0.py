from heapq import heappush, heappop
 
 class Solution:
     def kSmallestPairs(self, nums1, nums2, k):
         """
         :type nums1: List[int]
         :type nums2: List[int]
         :type k: int
         :rtype: List[List[int]]
         """
         heap = []
         def push(i, j):
             if i < len(nums1) and j < len(nums2):
                 heappush(heap, (nums1[i] + nums2[j], i, j))
         push(0,0)
         res = []
         while heap and len(res) < k:
             _, i, j = heappop(heap)
             res.append([nums1[i], nums2[j]])
             push(i, j+1)
             if j == 0:
                 push(i+1, 0)
         return res
