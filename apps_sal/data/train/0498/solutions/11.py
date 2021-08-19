class Solution:

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def helper(nums):
            steal = 0
            cool = 0
            for num in nums:
                (steal, cool) = (cool, max(cool, steal + num))
            return max(steal, cool)
        return max(helper(nums[:-1]), helper(nums[1:]))
