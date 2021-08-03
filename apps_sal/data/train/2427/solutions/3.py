class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        max_cnt = 0
        for x in nums:
            if x == 1:
                cnt += 1
            else:
                if max_cnt < cnt:
                    max_cnt = cnt
                cnt = 0
        if max_cnt < cnt:
            max_cnt = cnt
        return max_cnt
