class Solution:
     def containsNearbyDuplicate(self, nums, k):
         """
         :type nums: List[int]
         :type k: int
         :rtype: bool
         """
         last_seen_idx = {}
         for i, num in enumerate(nums):
             if num in last_seen_idx and i - last_seen_idx[num] <= k:
                 return True
             last_seen_idx[num] = i
         
         return False
