class Solution:

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None:
            return None
        if nums == []:
            return 0
        (start, end) = (0, len(nums) - 1)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > target:
                end = mid
            else:
                start = mid
        if nums[start] >= target:
            return start
        elif nums[end] >= target:
            return end
        else:
            return end + 1
