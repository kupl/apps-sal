class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        m = arr[(len(arr) - 1) // 2]
        (i, j) = (0, len(arr) - 1)
        while i + len(arr) - j <= k:
            if arr[j] - m >= m - arr[i]:
                j -= 1
            else:
                i += 1
        return arr[j + 1:] + arr[:i]
