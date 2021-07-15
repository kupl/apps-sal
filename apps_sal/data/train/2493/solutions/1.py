class Solution:
     def maximumProduct(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
         return max(a[0]*a[1]*a[2], a[0]*b[0]*b[1])
