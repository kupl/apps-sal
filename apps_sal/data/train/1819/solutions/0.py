class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.length = len(self.nums)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        first_idx = None
        idx_count = 0
        for i in range(self.length):
            if self.nums[i] == target:
                if first_idx is None:
                    first_idx = i
                idx_count += 1
            elif first_idx is not None:
                break
        if idx_count > 0:
            return int(idx_count * random.random() // 1) + first_idx
