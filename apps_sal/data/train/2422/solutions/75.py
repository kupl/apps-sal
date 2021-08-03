class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        current_max = -2147483647
        for i in range(n - 1):
            for j in range(i + 1, n):
                temp = (nums[i] - 1) * (nums[j] - 1)
                if(temp > current_max):
                    current_max = temp
        return current_max
