class Solution:
     def majorityElement(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         count = {}
         for i in nums:
             if i in count.keys():
                 count[i]+=1
             else:
                 count[i] = 1
         ans = count[nums[0]]
         res = nums[0]
         for x in count.keys():
             if count[x]>ans:
                 ans = count[x]
                 res = x
         return res
