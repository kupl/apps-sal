class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1

        while l <= r:
            mid = (l + r) // 2
            if mid > 0 and arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid

            if arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                r = mid - 1
