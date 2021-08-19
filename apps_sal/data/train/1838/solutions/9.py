class Solution:

    def maxChunksToSorted(self, arr):
        res = 0
        cur = arr[0]
        for (i, v) in enumerate(arr):
            if v > cur:
                cur = v
            if i == cur:
                res += 1
        return res
        '\n         :type arr: List[int]\n         :rtype: int\n         '
