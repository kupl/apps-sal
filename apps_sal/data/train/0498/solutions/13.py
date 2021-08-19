class Solution:

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        mark = [0 for i in range(len(nums))]
        result = list(mark)
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        mark[0] = 1
        result[0] = nums[0]
        if nums[0] > nums[1]:
            mark[1] = 1
            result[1] = nums[0]
        else:
            result[1] = nums[1]
        for i in range(2, len(nums)):
            result[i] = max(nums[i] + result[i - 2], result[i - 1])
            if nums[i] + result[i - 2] > result[i - 1]:
                mark[i] = mark[i - 2]
            else:
                mark[i] = mark[i - 1]
        if mark[0] == 1 and mark[-1] == 1:
            return max(self.solve(nums[1:]), self.solve(nums[:-1]))
        return result[-1]

    def solve(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        result = [0 for i in range(len(nums))]
        result[0] = nums[0]
        result[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            result[i] = max(nums[i] + result[i - 2], result[i - 1])
        return result[-1]
