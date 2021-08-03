class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        for i in range(n):
            nums.append(start + (2 * i))
        result = 0
        for n in nums:
            result = result ^ n
        return result
