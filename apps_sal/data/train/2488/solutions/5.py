class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ec = 0
        digit = 0
        for value in nums:
            digit = len(str(value))
            if digit % 2 == 0:
                ec += 1
        return ec
