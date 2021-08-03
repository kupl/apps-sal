class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        from itertools import combinations
        answer = None
        max_value = float('-inf')
        for x, y in combinations(list(range(len(nums))), 2):
            if (nums[x] * nums[y]) > max_value:
                answer = (nums[x] - 1) * (nums[y] - 1)
                max_value = nums[x] * nums[y]
        return answer
