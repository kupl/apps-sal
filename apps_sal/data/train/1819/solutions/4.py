class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        import random

        ans = -1
        idx = 0
        for i, num in enumerate(self.nums):
            if num == target:
                if ans == -1:
                    ans = i
                else:
                    if random.randint(0, idx) == 0:
                        ans = i
                idx += 1
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
