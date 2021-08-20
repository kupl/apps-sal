class Solution:

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best = 0
        total = 0
        for n in nums:
            if total + n < 0:
                total = 0
            else:
                total += n
            print(total)
            best = max(total, best)
        if max(nums) < 0:
            return max(nums)
        return best
