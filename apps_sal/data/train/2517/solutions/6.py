class Solution:

    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 1 if n else 0
        nums = [0] * (n + 1)
        nums[0] = 0
        nums[1] = 1
        nums[2] = 1
        for i in range(3, n + 1):
            nums[i] = nums[i - 1] + nums[i - 2] + nums[i - 3]
        return nums[n]
