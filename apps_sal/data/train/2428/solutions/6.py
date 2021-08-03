class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        s = set(nums)
        t = nums.copy()
        i = 0
        while s and i < len(t):
            if t[i] in s:
                s.remove(t.pop(i))
            else:
                i += 1
        return (set(nums) - set(t)).pop()
