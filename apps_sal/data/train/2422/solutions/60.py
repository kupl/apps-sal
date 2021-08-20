class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        candidates = [0, 0]
        highest = nums[0]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                if product > highest:
                    highest = product
                    candidates[0] = i
                    candidates[1] = j
        return (nums[candidates[0]] - 1) * (nums[candidates[1]] - 1)
