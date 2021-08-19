class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        res = []
        i = 0
        j = len(arr) - 1
        if j == 0:
            return arr
        median = arr[j // 2]
        while len(res) < k:
            if abs(median - arr[i]) <= abs(arr[j] - median):
                res.append(arr[j])
                j -= 1
            else:
                res.append(arr[i])
                i += 1
        return res
