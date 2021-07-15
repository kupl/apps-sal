class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low = 0
        high = len(arr) - 1
        
        while low < high:
            mid1 = (low + high)//2
            mid2 = mid1 + 1
            
            if arr[mid1] <= arr[mid2]:
                low = mid2
            else:
                high = mid1
        return low
