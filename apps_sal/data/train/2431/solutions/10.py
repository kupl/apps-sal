class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if len(nums) < 2 or k < 0:
            return 0

        count = 0
        nums.sort()
        i, j = 0, 1
        while i < len(nums) - 1 and j < len(nums):
            j = max(i + 1, j)
            d = nums[j] - nums[i]
            if d < k:
                j += 1
            elif d == k:
                count += 1
                while (i + 1) < len(nums) and nums[i] == nums[i + 1]:
                    i += 1
                i += 1
            else:
                i += 1

        return count
