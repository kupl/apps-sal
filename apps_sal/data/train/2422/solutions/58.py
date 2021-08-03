class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        k = nums[0]
        n = [i for i in range(2)]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] * nums[j] > k:
                    n[0] = nums[j]
                    n[1] = nums[i]
                    k = nums[i] * nums[j]
        m = ((n[0] - 1) * (n[1] - 1))
        return m
