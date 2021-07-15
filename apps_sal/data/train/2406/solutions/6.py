class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        for i in range(len(arr)):
            if i == 0 and arr[i] > arr[i + 1]:
                return i
            elif i == len(arr) - 1 and arr[i] > arr[i - 1]:
                return i
            elif arr[i] > arr[i + 1] and arr[i] > arr[i - 1]:
                return i
