class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                temp = (nums[i] - 1) * (nums[j] - 1)
                if temp > ans:
                    ans = temp
        return ans
