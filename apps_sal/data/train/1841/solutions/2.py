class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        m = arr[(n - 1) // 2]
        res = []
        (i, j) = (0, n - 1)
        while k > 0:
            if arr[j] - m >= m - arr[i]:
                res.append(arr[j])
                j -= 1
            else:
                res.append(arr[i])
                i += 1
            k -= 1
        return res
