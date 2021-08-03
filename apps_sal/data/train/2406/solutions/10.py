class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1

        while l < r:
            if arr[l] > arr[l + 1]:
                return l
            if arr[r - 1] < arr[r]:
                return r
            l, r = l + 1, r - 1
        return l
