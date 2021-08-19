class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        i = 0
        size = len(arr)
        # increasing check
        while i < size - 1 and arr[i] < arr[i + 1]:
            i += 1
        return i
