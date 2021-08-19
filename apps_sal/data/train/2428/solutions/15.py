class Solution:

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        a = Counter(nums)
        print(a)
        for (k, i) in list(a.items()):
            if i < 2:
                return k
