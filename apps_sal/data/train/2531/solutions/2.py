class Solution:
     def findUnsortedSubarray(self, nums):
         if len(nums) == 1:
             return 0
         
         start = -1
         end = -1
         for i in range(len(nums)-1):
             if nums[i] > nums[i+1]:
                 start = i
                 break
         for i in reversed(list(range(1,len(nums)))):
             if nums[i] < nums[i-1]:
                 end = i
                 break
         if start == -1:
             return 0
         
         minimum = 10000000000000
         maximum = -10000000000000
         
         for i in range(start, end+1):
             if nums[i] > maximum:
                 maximum = nums[i]
             if nums[i] < minimum:
                 minimum = nums[i]
         
         for i in range(0, len(nums)):
             if nums[i] > minimum:
                 start = i
                 break
         for i in reversed(list(range(len(nums)))):
             if nums[i] < maximum:
                 end = i
                 break
         return end - start + 1
             

