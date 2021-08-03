class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums[0], nums[-1])

        a = [0 for _ in range(len(nums) - 1)]
        b = a.copy()
        c = b.copy()
        a[0] = nums[0]
        b[0] = nums[-1]

        for i in range(1, len(nums) - 1):
            a[i] = max(a[i - 1], a[i - 2] + nums[i])
            b[i] = max(b[i - 1], b[i - 2] + nums[-i - 1])
        return max(a[-1], b[-1])
