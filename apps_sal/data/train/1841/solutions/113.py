class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr = sorted(arr)
        i, j, res = 0, len(arr), []
        median = arr[(j - 1) // 2]

        while len(res) < k:
            if abs(arr[j - 1] - median) >= abs(arr[i] - median):
                res.append(arr[j - 1])
                j -= 1
            else:
                res.append(arr[i])
                i += 1
        return res
