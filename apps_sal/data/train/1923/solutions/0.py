class Solution:

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = sorted(nums)
        c = []
        for n in nums:
            p = bisect.bisect_left(s, n)
            c.append(p)
            s.pop(p)
        return c
