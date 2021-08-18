class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)
        while l < r:
            m = (l + r) // 2
            if arr[m - 1] < arr[m] > arr[m + 1]:
                return m
            if arr[m] < arr[m + 1]:
                l = m + 1
            else:
                r = m
        return l


'''
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return arr.index(max(arr))
'''
