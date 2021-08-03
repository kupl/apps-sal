class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lens = len(nums)
        t = nums
        t = sorted(t)
        print(nums)
        t1 = lens
        t2 = 0
        for i in range(lens - 1):
            if nums[i] != t[i]:
                t1 = i
                break
        for i in range(lens - 1, 0, -1):
            if nums[i] != t[i]:
                t2 = i
                break
        print(t2)
        return max(t2 - t1 + 1, 0)
