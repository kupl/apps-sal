class Solution:
     def findUnsortedSubarray(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         sort_nums = sorted(nums)
         diff = list(map(lambda x, y: x - y, sort_nums, nums))
         start, end = 0, len(nums) - 1
         while start < end:
             if diff[start] == 0:
                 start += 1
                 
             if diff[end] == 0:
                 end -= 1
             
             if diff[start] and diff[end]:
                 break
         
         if end > start:
             return end - start + 1
         else:
             return 0

