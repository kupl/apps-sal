class Solution:

    def missingNumber(self, nums):
        return sum(range(len(nums) + 1)) - sum(nums)
        ' \n         :type nums: List[int]\n         :rtype: int\n         '
