class Solution:

    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        from collections import Counter
        c = Counter(nums)
        if k == 0:
            return sum([1 for (num, count) in list(c.items()) if count > 1])
        else:
            return sum([1 for (num, _) in list(c.items()) if num + k in c])
