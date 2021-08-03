class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_nums = []
        for i in range(2):
            for num in nums:
                if num == max(nums):
                    max_nums.append(num - 1)
                    nums.remove(num)
        return max_nums[0] * max_nums[1]
