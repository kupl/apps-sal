class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 1:
            return nums[0]

        # Attempt 1 - 80%
        # nums.sort()
        # i = 0
        # while i < l:
        #     if i+1 == l:
        #         return nums[i]
        #     elif nums[i] != nums[i+1]:
        #         #either i or i+1
        #         if nums[i+2] == nums[i+1]:
        #             return nums[i]
        #     else:
        #         i+=2

        # Attempt 2 - 100%
        result = 0
        for num in nums:
            result ^= num
        return result
