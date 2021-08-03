class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        def binarysearch(arr):
            low = 0
            high = len(arr) - 1

            while low <= high:
                mid = (low + high) // 2
                if arr[mid] < 0:
                    high = mid - 1
                else:
                    low = mid + 1
            return low
        count = 0
        for arr in grid:
            val = binarysearch(arr)
            count += len(arr) - val
        return count
