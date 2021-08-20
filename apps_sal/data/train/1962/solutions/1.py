class Solution:

    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = 0
        s_max = 0
        max_num_index = 0
        if len(nums) != 1:
            for i in range(len(nums)):
                if nums[i] > max_num:
                    s_max = max_num
                    s_max_index = max_num_index
                    max_num = nums[i]
                    max_num_index = i
                elif nums[i] > s_max:
                    s_max = nums[i]
            if max_num >= 2 * s_max:
                return max_num_index
            else:
                return -1
        else:
            return 0
