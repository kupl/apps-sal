class Solution:

    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            count = 0
            while num:
                num = num // 10
                count += 1
            if count % 2 == 0:
                result += 1
        return result
