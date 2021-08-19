# O(logn), binary search for peak since arr is ordered
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)
        while l < r:
            m = (l + r) // 2
            if arr[m - 1] < arr[m] > arr[m + 1]:
                return m
            if arr[m] < arr[m + 1]:  # peak on right
                l = m + 1
            else:  # peak on left
                r = m
        return l


'''
# O(n), distinct elements so get max and return it's index
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return arr.index(max(arr))
'''
