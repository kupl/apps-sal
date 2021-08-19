class Solution:

    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l < 3:
            return -1
        s = [0] * l
        s[0] = nums[0]
        for i in range(1, l):
            s[i] = s[i - 1] + nums[i]
        d = [0] * l
        d[l - 1] = nums[l - 1]
        for j in range(l - 2, -1, -1):
            d[j] = d[j + 1] + nums[j]
        for i in range(0, l):
            if s[i] == d[i]:
                return i
        return -1
