class Solution:
    def findSpecialInteger(self, nums: List[int]) -> int:
        percent = len(nums) * 0.25
        for I in nums:
            if nums.count(I) > percent:
                return I
