class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        m = -1
        ans = 0
        for i, num in enumerate(arr):
            m = max(num, m)
            if m == i:
                ans += 1
        return ans
