class Solution:

    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ret = 0
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cnt += 1
            else:
                ret = max(ret, cnt)
                cnt = 1
        return max(ret, cnt)
