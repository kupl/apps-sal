class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()

        for i in range(1, len(nums)):
            print(i)

            if nums[i] == nums[i - 1]:
                return True

        return False
