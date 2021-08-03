class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int

        If is increasing then it is chunkable.
        It if decreases then no.

        We start with one chunk (the whole array)
        """
        total_chunks = 0
        max_so_far = 0
        for i, val in enumerate(arr):
            max_so_far = max(max_so_far, val)
            if max_so_far == i:
                total_chunks += 1

        return total_chunks
