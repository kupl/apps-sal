class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxValue = 0
        max_return = 0
        for nr_idx in range(len(nums)):
            for nr_id in range(nr_idx + 1, len(nums)):
                if nr_id != nr_idx:
                    max_Value = (nums[nr_idx] - 1) * (nums[nr_id] - 1)
                    if max_Value > max_return:
                        max_return = max_Value
        return max_return
