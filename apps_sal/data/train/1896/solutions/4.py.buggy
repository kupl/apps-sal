import heapq
 class Solution:
     def kSmallestPairs(self, nums1, nums2, k):
         """
         :type nums1: List[int]
         :type nums2: List[int]
         :type k: int
         :rtype: List[List[int]]
         """
         pq = []
         m, n = len(nums1), len(nums2)   # get lenth
         if m == 0 or n == 0:            # if one of the list is empty return []
             return []
         for i in range(m):              # get through the first list
             if len(pq) == k and pq[0][0] > -nums1[i]-nums2[0]: # stop if larger than current k
                 break
             for j in range(n):          # go throught the second list
                 s = -nums1[i]-nums2[j]   # get the sum
                 if len(pq) < k or pq[0][0] < s: # if less than k or less than current k
                     heapq.heappush(pq, (s, [nums1[i], nums2[j]]))   # push 
                     if len(pq) > k: # get it out
                         heapq.heappop(pq)
                 else:                   # stop if larger than current k
                     break
         return [item[1] for item in pq]
         
