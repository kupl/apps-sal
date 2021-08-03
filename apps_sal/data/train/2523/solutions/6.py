class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = {}
        se = {}
        cur_max_cnt = 0
        cur_span = float('inf')
        for idx, n in enumerate(nums):
            if not n in se:
                se[n] = [idx, idx]
                cnt[n] = 1
            else:
                se[n][1] = idx
                cnt[n] += 1
            x, y = se[n]
            if cnt[n] > cur_max_cnt or (cnt[n] == cur_max_cnt and y - x + 1 < cur_span):
                cur_max_cnt = cnt[n]
                cur_span = y - x + 1
        return cur_span
