class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        if n % 2:
            find = set(nums[0:(n // 2) + 1]) & set(nums[n // 2:])
        else:
            find = set(nums[0:n // 2]) & set(nums[n // 2:])

        for i in find:
            if nums.count(i) > n // 2:
                return i
