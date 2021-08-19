class Solution:

    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        chunks = 0
        max_this_chunk = 0
        for (index, num) in enumerate(arr):
            if num > max_this_chunk:
                max_this_chunk = num
            if max_this_chunk <= index:
                chunks += 1
                max_this_chunk = 0
        return chunks
