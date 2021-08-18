class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        t = arr[0]
        left_max = []

        for x in arr:
            t = max(t, x)
            left_max.append(t)

        t = arr[-1]
        right_min = []
        for i in range(len(arr) - 1, -1, -1):
            t = min(arr[i], t)
            right_min.append(t)

        count = 1

        for i in range(0, len(arr) - 1):
            if left_max[i] <= right_min[len(arr) - i - 2]:
                count += 1

        return count
