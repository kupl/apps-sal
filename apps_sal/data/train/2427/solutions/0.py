class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0

        count = 0
        countMax = 0
        for ele in nums:
            if ele == 1:
                count += 1
            else:
                if count > countMax:
                    countMax = count
                count = 0

        if count > countMax:
            countMax = count

        return countMax
