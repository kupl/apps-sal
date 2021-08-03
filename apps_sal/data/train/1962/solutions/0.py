class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        m = max(nums)
        ind = nums.index(m)
        del nums[ind]
        m_2 = max(nums)
        return ind if m >= 2 * m_2 else -1
