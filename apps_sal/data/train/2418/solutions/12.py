class Solution:
     def containsDuplicate(self,nums):
         if(len(nums)>1):
             count=0
             giru=[]
             nums.sort()
             for i in range(len(nums)):
                 if i+1<len(nums):
                     if(nums[i]==nums[i+1]):
                         count=count+1
 
             if(count>0):
                 return True
             else: return False
         else :
             return False
             """
         :type nums: List[int]
         :rtype: bool
         """

