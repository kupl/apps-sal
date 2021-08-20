class Solution:

    def xorOperation(self, n: int, start: int) -> int:
        nums = [0] * n
        res = 0
        for i in range(n):
            nums[i] = start + 2 * i
            res = res ^ nums[i]
        return res
