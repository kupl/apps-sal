class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        nums = list(range(1, N + 1))

        def helper(nums):
            if len(nums) < 3:
                return nums
            odd = nums[::2]
            even = nums[1::2]
            return helper(even) + helper(odd)
        return helper(nums)
