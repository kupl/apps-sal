class Solution:
     def containsNearbyDuplicate(self, nums, k):
         """
         :type nums: List[int]
         :type k: int
         :rtype: bool
         """
         if not nums:
             return False
         d = collections.defaultdict(list)
         for i, n in enumerate(nums):
             if n in d:
                 for index in d[n]:
                     if i - index <= k:
                         return True
             d[n].append(i)
         return False
