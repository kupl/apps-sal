class Solution:

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while True:
            mid = (left + right) // 2
            if arr[mid] > arr[mid - 1] and arr[mid + 1] > arr[mid]:
                left = mid
            elif arr[mid] < arr[mid - 1] and arr[mid + 1] < arr[mid]:
                right = mid
            else:
                return mid
