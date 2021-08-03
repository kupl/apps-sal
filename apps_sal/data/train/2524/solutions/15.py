class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 1
        L = []
        if len(nums) >= 2:
            for i in range(0, len(nums) - 1):
                if nums[i + 1] > nums[i]:
                    counter += 1
                else:
                    counter = 1
                L.append(counter)
            return max(L)
        elif len(nums) == 1:
            return 1
        else:
            return 0
