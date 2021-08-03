class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n, lst = len(nums), sorted(nums)
        for i in range(n):
            if lst[i] != nums[i]:
                L = i
                break
        else:
            return 0
        for i in range(n - 1, -1, -1):
            if lst[i] != nums[i]:
                R = i
                break
        return R - L + 1
