class Solution:

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(nums[0])
        for i in range(len(nums)):
            v = nums[i]
            while v != nums[v]:
                (nums[v], v) = (v, nums[v])
        for (i, num) in enumerate(nums):
            if i != num:
                return i
        return None
