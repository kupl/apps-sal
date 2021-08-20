class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        if nums == []:
            return None
        max = None
        for (idx, i) in enumerate(nums):
            j = idx + 1
            while j < len(nums):
                product = (i - 1) * (nums[j] - 1)
                if max == None:
                    max = product
                elif product > max:
                    max = product
                j += 1
        return max
