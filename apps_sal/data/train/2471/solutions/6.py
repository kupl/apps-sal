class Solution:

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        l1 = [0] * n
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        (l1[0], l1[1]) = (nums[0], max(nums[0], nums[1]))
        for i in range(2, n):
            l1[i] = max(l1[i - 1], nums[i] + l1[i - 2])
        return max(l1)
