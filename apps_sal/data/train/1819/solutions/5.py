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
        res = None
        ct = 0
        for (i, x) in enumerate(self.nums):
            if x == target:
                ct += 1
                pb = random.randint(1, ct)
                if pb == ct:
                    res = i
        return res
