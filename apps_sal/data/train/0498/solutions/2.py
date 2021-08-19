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
        if len(nums) <= 3:
            return max(nums)

        def rob_line(lst):
            (last, now) = (0, 0)
            for i in lst:
                (last, now) = (now, max(now, last + i))
            return now
        return max(rob_line(nums[:-1]), rob_line(nums[1:]))
