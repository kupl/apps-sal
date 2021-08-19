class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        i = nums[0]
        j = nums[1]
        for num in range(2, len(nums)):
            if nums[num] > i or nums[num] > j:
                if nums[num] > i:
                    if i > j:
                        j = i
                    i = nums[num]
                else:
                    if j > i:
                        i = j
                    j = nums[num]
        return (i - 1) * (j - 1)
