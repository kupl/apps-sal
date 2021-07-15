class Solution:
     def maximumProduct(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         h, m, l = -float('inf'), -float('inf'), -float('inf')
         lowest, second_lowest = float('inf'), float('inf')
         
         for num in nums:
             if num > h:
                 l = m
                 m = h
                 h= num
             elif num > m:
                 l = m
                 m = num
             elif num > l:
                 l = num
                 
             if num < lowest:
                 second_lowest = lowest
                 lowest = num
             elif num < second_lowest:
                 second_lowest = num
                 
         return max(h*m*l, h*lowest*second_lowest)
