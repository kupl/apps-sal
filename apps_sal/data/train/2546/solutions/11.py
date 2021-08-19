class Solution:

    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairCount = 0
        i = 0
        while i < len(nums) - 1:
            j = i + 1
            while j < len(nums):
                if nums[i] == nums[j]:
                    pairCount += 1
                j += 1
            i += 1
        return pairCount
