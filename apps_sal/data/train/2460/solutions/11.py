class Solution:
     def maxSubArray(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         # [-2,1,-3,-5]
         curSum = maxSum = nums[0]
         for num in nums[1:]:
             curSum = max(num, curSum + num) # start a new array or use added up array num[1]=1 or num[0]+num[1]=-1
             maxSum = max(maxSum, curSum) # update the max prior = 1 or cursum 1-3-5
 
         return maxSum

