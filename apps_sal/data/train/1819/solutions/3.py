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
        if len(self.nums) == 1:
            return 0

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
