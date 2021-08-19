class Solution:

    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if arr is None:
            return 0
        if len(arr) < 2:
            return len(arr)
        suffix_min = [float('inf')] * len(arr)
        suffix_min[-1] = arr[-1]
        suffix_max = [float('-inf')] * len(arr)
        suffix_max[-1] = arr[-1]
        for index in range(len(arr) - 2, -1, -1):
            suffix_min[index] = min(arr[index + 1], suffix_min[index + 1])
            suffix_max[index] = max(arr[index + 1], suffix_max[index + 1])
        index = 0
        chunk_count = 0
        print(suffix_min)
        while index < len(arr):
            chunk_count += 1
            if arr[index] > suffix_min[index]:
                j = index
                running_max = arr[j]
                while j < len(arr) and running_max > suffix_min[j]:
                    running_max = max(running_max, arr[j])
                    j += 1
                index = j + 1
            else:
                index += 1
        return chunk_count
