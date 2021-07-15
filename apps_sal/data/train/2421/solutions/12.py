class Solution:
     def majorityElement(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         s = {}
         for i in range(len(nums)):
             s[nums[i]] = s.get(nums[i], 0) + 1
         
         for num in nums:
             if s[num] > len(nums) // 2:
                 return num
                 
         
        
         

