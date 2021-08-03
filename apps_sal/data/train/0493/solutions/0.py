class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        c = [0] * 1001
        c[0] = 1
        T = sum(nums)
        A = T + S
        if T < S or A & 1:
            return 0
        A >>= 1
        nums = sorted(nums)
        temp = 0
        for ind, v in enumerate(nums):
            temp += v
            for i in range(min(temp, A), v - 1, -1):
                c[i] += c[i - v]
        return c[A]
