class Solution:

    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n - 1
        im = 0
        im2 = 1
        if nums[im2] > nums[im]:
            (im, im2) = (im2, im)
        for i in range(2, n):
            if nums[i] > nums[im]:
                im2 = im
                im = i
            elif nums[i] > nums[im2]:
                im2 = i
        if nums[im] >= nums[im2] * 2:
            return im
        else:
            return -1
