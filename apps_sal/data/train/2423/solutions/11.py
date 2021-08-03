class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_sum = 0
        temp = 0
        for num in nums:
            temp += num
            min_sum = min(temp, min_sum)

        return abs(min_sum) + 1
