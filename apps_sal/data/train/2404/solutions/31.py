class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:  # good 2, check the diff between idx and element, then compare to k, time O(logn), space O(1)
        l, r = 0, len(arr) - 1
        while l < r:  # find the last idx whose diff from the num is <k+1
            m = (l + r) // 2
            if arr[m] - m >= k + 1:
                r = m - 1
            else:
                l = m + 1

        if arr[l] - l < k + 1:
            return l + k + 1  # arr[l]+(k+1)-(arr[l]-l)
        else:
            return l + k  # arr[l-1]+(k+1)-(arr[l-1]-l+1)
