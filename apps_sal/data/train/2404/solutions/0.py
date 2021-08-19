class Solution:

    def findKthPositive(self, arr: List[int], k: int) -> int:
        (lo, hi) = (0, len(arr) - 1)
        while lo < hi:
            mid = hi - (hi - lo) // 2
            missing = arr[mid] - mid - 1
            if missing < k:
                lo = mid
            else:
                hi = mid - 1
        if arr[lo] - lo - 1 >= k:
            return k
        else:
            return k + lo + 1
