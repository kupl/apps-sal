class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sumlist = [0] * (len(nums) + 1)
        sumlist[0] = 0
        sumMin = 0
        globalMax = nums[0]
        for i in range(1, len(nums) + 1):
            sumlist[i] = sumlist[i - 1] + nums[i - 1]
            print(sumlist[i])
            globalMax = max(sumlist[i] - sumMin, globalMax)
            sumMin = min(sumMin, sumlist[i])

        return globalMax
