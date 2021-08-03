class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        cnt, sm, ism = 0, 0, 0
        for i, num in enumerate(arr):
            sm += num
            ism += i
            if sm == ism:
                cnt += 1
        return cnt
