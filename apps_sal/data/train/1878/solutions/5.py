class Solution:

    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr_index = sorted(list(range(len(arr))), key=arr.__getitem__)
        ans = ma = 0
        for (i, x) in enumerate(arr_index):
            ma = max(ma, x)
            if ma == i:
                ans += 1
        return ans
