class Solution:
     def containsNearbyDuplicate(self, nums, k):
         if not nums or k<0 or len(nums)==len(set(nums)):
             return False
         mapD={}
         for i,v in enumerate(nums):
             if v in mapD and i-mapD[v]<=k:
                 return True
             mapD[v]=i
         return False
             

