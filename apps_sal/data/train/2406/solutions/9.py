class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while l <= r:
            m = l + (r - l) // 2
            if m + 1 < len(arr) and arr[m] < arr[m + 1]:
                l = m + 1
            else:
                r = m - 1
        return l
