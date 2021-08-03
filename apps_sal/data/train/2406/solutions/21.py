class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        i, j = 0, len(arr) - 1
        while i < j:
            m = (i + j) // 2
            if arr[m] > arr[m + 1]:
                j = m
            else:
                i = m + 1
        return i
