class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        m = arr[(len(arr) - 1) // 2]
        l, r = 0, len(arr) - 1
        res = []
        while len(res) < k:
            if abs(arr[l] - m) > abs(arr[r] - m):
                res.append(arr[l])
                l = l + 1
            else:
                res.append(arr[r])
                r = r - 1
        return res
