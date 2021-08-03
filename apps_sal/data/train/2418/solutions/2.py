class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()

        if len(nums) - 1 == 1:
            if nums[0] == nums[1]:
                return True

        for i in range(1, len(nums)):
            print(i)

            if nums[i] == nums[i - 1]:
                return True

        return False
