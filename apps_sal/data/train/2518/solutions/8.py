class Solution:

    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        decreasing = []
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                decreasing.append(i)
        if not decreasing:
            return True
        if len(decreasing) > 1:
            return False

        def check(array):
            n = len(array)
            for i in range(n - 1):
                if array[i] > array[i + 1]:
                    return False
            return True
        i = decreasing[0]
        temp = nums[i]
        nums[i] = nums[i + 1]
        if check(nums):
            return True
        nums[i] = temp
        nums[i + 1] = nums[i]
        if check(nums):
            return True
        return False
