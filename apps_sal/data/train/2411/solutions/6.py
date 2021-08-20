class Solution:

    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max3 = [nums[0], None, None]
        for i in range(1, len(nums)):
            if nums[i] in max3:
                continue
            if nums[i] > max3[0]:
                max3 = [nums[i], max3[0], max3[1]]
            elif max3[1] is None or nums[i] > max3[1]:
                max3 = [max3[0], nums[i], max3[1]]
            elif max3[2] is None or nums[i] > max3[2]:
                max3 = [max3[0], max3[1], nums[i]]
            else:
                continue
        if None in max3:
            return max3[0]
        else:
            return max3[2]
