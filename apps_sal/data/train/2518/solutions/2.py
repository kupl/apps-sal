class Solution:

    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        if len(nums) == 1:
            return True
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if nums[i + 1] < nums[i - 1] and i - 1 >= 0:
                    count += 1
                    if i + 1 != len(nums) - 1:
                        nums[i + 1] = nums[i]
                else:
                    nums[i] = nums[i + 1]
                    count += 1
                    if count == 1:
                        nums[i] -= 1
        if count > 1:
            return False
        else:
            return True
