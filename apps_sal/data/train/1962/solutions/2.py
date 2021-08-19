class Solution:

    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        maxval = nums[0]
        maxindex = 0
        secVal = None
        for (i, e) in enumerate(nums):
            if i == 0:
                continue
            if e > maxval:
                (secVal, maxval) = (maxval, e)
                maxindex = i
            elif secVal is None:
                secVal = e
            elif e > secVal:
                secVal = e
        if secVal * 2 <= maxval:
            return maxindex
        return -1
