class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = sorted(nums)
        start = -1
        end = -1
        for i in range(len(a)):
            if a[i] != nums[i] and start == -1:
                start = i
            elif a[i] != nums[i]:
                end = i

        if start == -1:
            return 0

        return end - start + 1
