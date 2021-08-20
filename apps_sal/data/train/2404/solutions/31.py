class Solution:

    def findKthPositive(self, arr: List[int], k: int) -> int:
        (l, r) = (0, len(arr) - 1)
        while l < r:
            m = (l + r) // 2
            if arr[m] - m >= k + 1:
                r = m - 1
            else:
                l = m + 1
        if arr[l] - l < k + 1:
            return l + k + 1
        else:
            return l + k
