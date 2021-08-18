class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.length = len(nums)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        result, index = self.nums.index(target), 1
        for i in range(self.length):
            num = self.nums[i]
            if num == target and random.randint(0, index) is 0:
                result = i
                index += 1
        return result
