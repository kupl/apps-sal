class Solution:

    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        n = 1
        ans = [1]
        for i in range(0, len(nums) - 1):
            if nums[i + 1] > nums[i]:
                n += 1
            else:
                ans.append(n)
                n = 1
            if i == len(nums) - 2:
                ans.append(n)
        return max(ans)
