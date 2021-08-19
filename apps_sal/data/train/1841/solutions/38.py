from collections import defaultdict


class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr = sorted(arr)
        n = len(arr)
        median = arr[(n - 1) // 2]
        (l, r) = (0, n - 1)
        res = []
        for i in range(k):
            if abs(arr[l] - median) > abs(arr[r] - median):
                res.append(arr[l])
                l += 1
            else:
                res.append(arr[r])
                r -= 1
        return res
