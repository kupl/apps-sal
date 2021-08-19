class Solution:

    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        out_index = -1
        (lrgst, scnd, ind) = (-float('inf'), None, None)
        for i in range(len(nums)):
            if nums[i] > lrgst:
                (lrgst, scnd, ind) = (nums[i], lrgst, i)
            elif nums[i] > scnd:
                scnd = nums[i]
        if lrgst >= 2 * scnd:
            out_index = ind
        return out_index
