class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        while arr[l] < arr[l + 1]:
            l += 1
        return l
