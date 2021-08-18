class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[left] < arr[left + 1]:
                left += 1
            if arr[right] < arr[right - 1]:
                right -= 1
            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid

        return mid
