class Solution:

    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        max = 0
        rtype = 0
        for i in range(0, len(arr)):
            if arr[i] > max:
                max = arr[i]
            if max == i:
                rtype = rtype + 1
        return rtype
