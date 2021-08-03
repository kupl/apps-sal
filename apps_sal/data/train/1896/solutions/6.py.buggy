import heapq
 
 class Solution:
     def kSmallestPairs(self, nums1, nums2, k):
         """
         :type nums1: List[int]
         :type nums2: List[int]
         :type k: int
         :rtype: List[List[int]]
         """
         
         if not nums1 or not nums2:
             return []
         
         index = [0 for _ in range(len(nums1))]
         q = [[nums1[i] + nums2[index[i]], i] for i in range(len(nums1))]
         heapq.heapify(q)
         i = 0
         ans = []
         while i < k and i < len(nums1) * len(nums2):
             pair = heapq.heappop(q)
             ans.append([nums1[pair[1]], nums2[index[pair[1]]]])
             i += 1
             if index[pair[1]] + 1 < len(nums2):
                 index[pair[1]] += 1
                 heapq.heappush(q, [nums1[pair[1]] + nums2[index[pair[1]]], pair[1]])
             
         return ans
             
         
