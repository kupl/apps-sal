class Solution:
     def findLengthOfLCIS(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         
         if nums == []:
             return 0
         longest = 1
         curr = 1
         
         for i in range(0,len(nums)-1):
             if nums[i]<nums[i+1]:
                 curr +=1
                 print(curr)
             else:
                 
                 longest = max(longest,curr)
                 curr = 1
         longest = max(longest,curr)
         return longest
