class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        sum = 0
        for (i, num) in enumerate(nums):
            j = i + 1
            while j < len(nums):
                tempSum = (nums[i] - 1) * (nums[j] - 1)
                if sum < tempSum:
                    sum = tempSum
                j = j + 1
        return sum
