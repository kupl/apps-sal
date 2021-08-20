class Solution:

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        hi = len(arr) - 1
        lo = 0
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid - 1] >= arr[mid]:
                hi = mid
            else:
                lo = mid
