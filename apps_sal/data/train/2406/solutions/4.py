class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1
        while l < r:
            if arr[r-1] >= arr[r]:
                r -= 1
            if arr[l + 1] >= arr[l]:
                l += 1
        return r
