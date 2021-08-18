class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        maxx, chunkCount = 0, 0
        for i in range(len(arr)):
            maxx = max(maxx, arr[i])
            if i >= maxx:
                chunkCount += 1

        return chunkCount
