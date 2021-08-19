class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        res = []
        arr.sort()
        j = len(arr) - 1
        if j == 0:
            return arr
        median = arr[j // 2]
        i = 0
        count = 1
        while count <= k:
            if abs(arr[i] - median) > abs(arr[j] - median):
                res.append(arr[i])
                i += 1
            elif abs(arr[i] - median) == abs(arr[j] - median):
                res.append(arr[j])
                j -= 1
            else:
                res.append(arr[j])
                j -= 1
            count += 1
        return res
