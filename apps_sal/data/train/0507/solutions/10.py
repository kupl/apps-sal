class Solution:

    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        startIndex = 0
        endIndex = len(nums) - 1
        while startIndex < endIndex:
            midIndex = (endIndex - startIndex) // 2 + startIndex
            midValue = nums[midIndex]
            leftValue = nums[midIndex - 1] if midIndex - 1 >= 0 else None
            rightValue = nums[midIndex + 1] if midIndex + 1 < len(nums) else None
            numLeftUnknowns = midIndex
            numRightUnknowns = len(nums) - 1 - midIndex
            if leftValue != midValue and rightValue != midValue:
                return midValue
            elif leftValue == midValue:
                numLeftUnknowns -= 1
            else:
                numRightUnknowns -= 1
            if numLeftUnknowns % 2 != 0:
                endIndex = midIndex - 1
            else:
                startIndex = midIndex + 1
        return nums[startIndex]
