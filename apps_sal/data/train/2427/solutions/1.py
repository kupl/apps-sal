class Solution:
     def findMaxConsecutiveOnes(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         cur=0
         ans=0
         for num in nums:
             if num==1:
                 cur=cur+1
                 ans = max(ans,cur)
             else:cur=0
         return ans
                 
         

