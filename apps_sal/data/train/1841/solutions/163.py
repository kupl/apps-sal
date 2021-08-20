class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        m = arr[(n - 1) // 2]
        res = []
        (l, r) = (0, n - 1)
        for i in range(k):
            if abs(arr[r] - m) >= abs(arr[l] - m):
                res.append(arr[r])
                r -= 1
            else:
                res.append(arr[l])
                l += 1
        return res
