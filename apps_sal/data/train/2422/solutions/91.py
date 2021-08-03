class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        d = len(nums)
        m = None

        for i in range(d):
            for j in range(i + 1, d):
                mn = (nums[i] - 1) * (nums[j] - 1)
                if m is None:
                    m = mn
                elif m < mn:
                    m = mn
        return m
