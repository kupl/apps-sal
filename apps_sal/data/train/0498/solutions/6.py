class Solution:

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mem = {}

        def max_money(start, rob_first=False):
            if start >= len(nums):
                return 0
            if start == len(nums) - 1 and rob_first:
                return 0
            if (start, rob_first) in mem:
                return mem[start, rob_first]
            if start == 0:
                mem[start, rob_first] = max(max_money(start + 1, False), nums[start] + max_money(start + 2, True))
            else:
                mem[start, rob_first] = max(max_money(start + 1, rob_first), nums[start] + max_money(start + 2, rob_first))
            return mem[start, rob_first]
        return max_money(0)
