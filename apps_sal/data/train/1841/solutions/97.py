class Solution:

    def getStrongest(self, arr, k):
        n = len(arr)
        arr = sorted(arr)
        m = arr[(n - 1) // 2]
        (i, j) = (0, n - 1)
        while k > 0:
            if arr[j] - m >= m - arr[i]:
                j -= 1
            else:
                i += 1
            k -= 1
        return arr[:i] + arr[j + 1:]
