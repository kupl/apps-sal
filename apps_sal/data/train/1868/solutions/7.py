class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        nums = []
        for i in range(1, N + 1):
            nums.append(i)

        def div(nums):
            if len(nums) < 3:
                return nums
            odd = nums[1::2]
            even = nums[::2]
            return div(even) + div(odd)
        return div(nums)
