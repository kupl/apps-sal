class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        (first, second) = (0, 0)
        for number in nums:
            if number > first:
                (first, second) = (number, first)
            else:
                second = max(number, second)
        return (first - 1) * (second - 1)
