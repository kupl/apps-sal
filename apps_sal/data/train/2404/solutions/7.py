class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        def bsearch(arr, val):
            low, high = 0, len(arr) - 1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] < val:
                    low = mid + 1
                elif arr[mid] > val:
                    high = mid - 1
                else:
                    return mid
            return -1
        count = 0
        max_int = max(arr)
        for i in range(1, max_int + k + 1):
            if bsearch(arr, i) == -1:
                count += 1
                print(i)
            if count == k:
                return i
