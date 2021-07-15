class Solution:
     def kSmallestPairs(self, nums1, nums2, k):
         """
         :type nums1: List[int]
         :type nums2: List[int]
         :type k: int
         :rtype: List[List[int]]
         """
         result = []
         import heapq
         m = len(nums1)
         n = len(nums2)
         if m*n>0:
             used = [[0 for _ in range(n)] for _ in range(m)]
             used[0][0] = 1
             h = [(nums1[0]+nums2[0],(0,0))]
             while k  > 0 and h:
                 _,(s1,s2) = heapq.heappop(h)
                 result.append([nums1[s1],nums2[s2]])
                 if s1+1 < m and used[s1+1][s2] == 0:
                     heapq.heappush(h,(nums1[s1+1]+nums2[s2],(s1+1,s2)))
                     used[s1+1][s2] = 1
                 if s2+1 < n and used[s1][s2+1] == 0:
                     heapq.heappush(h,(nums1[s1]+nums2[s2+1],(s1,s2+1)))
                     used[s1][s2+1] = 1
                 k -= 1
         return result

