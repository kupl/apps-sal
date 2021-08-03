class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        seq, max_seq = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                seq += 1
            else:
                max_seq = max(max_seq, seq)
                seq = 1
        max_seq = max(max_seq, seq)
        return max_seq
