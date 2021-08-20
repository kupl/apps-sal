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


"\n# O(n), distinct elements so get max and return it's index\nclass Solution:\n    def peakIndexInMountainArray(self, arr: List[int]) -> int:\n        return arr.index(max(arr))\n"
