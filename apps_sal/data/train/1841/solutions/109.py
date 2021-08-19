class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        median = arr[(len(arr) - 1) // 2]
        (i, j) = (0, len(arr) - 1)
        res = []
        while i <= j and k:
            if abs(arr[i] - median) > abs(arr[j] - median):
                res.append(arr[i])
                i += 1
            else:
                res.append(arr[j])
                j -= 1
            k -= 1
        return res
