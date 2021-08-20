class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        max_val = 0
        curr_val = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if i == 0 and j == 0:
                    max_val = (nums[i] - 1) * (nums[j] - 1)
                else:
                    curr_val = (nums[i] - 1) * (nums[j] - 1)
                    if curr_val > max_val:
                        max_val = curr_val
        return max_val
