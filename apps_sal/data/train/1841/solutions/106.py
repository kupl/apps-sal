class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        median = arr[(n - 1) // 2]
        i, j = 0, n - 1
        res = []
        while i <= j:
            if abs(arr[j] - median) >= abs(arr[i] - median):
                res.append(arr[j])
                j -= 1
            else:
                res.append(arr[i])
                i += 1
            if len(res) == k:
                return res
