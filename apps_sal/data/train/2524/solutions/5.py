class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if nums == []:
        #     return 0
        # ans,n = 1,1
        # for i in range(len(nums)-1):
        #     if nums[i+1]>nums[i]:
        #         n += 1
        #         ans = max(ans,n)
        #     else:
        #         n = 1
        # return ans
        ans = anchor = 0
        for i in range(len(nums)):
            if i and nums[i - 1] >= nums[i]:
                anchor = i
            ans = max(ans, i - anchor + 1)
        return ans
