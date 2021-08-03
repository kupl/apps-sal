class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return sum(list(map(lambda t: t[0] - t[1] < 0, zip(nums[1:], nums[:-1])))) <= 1 and sum(list(map(lambda t: t[0] - t[1] < 0, zip(nums[2:], nums[:-2])))) <= 1
