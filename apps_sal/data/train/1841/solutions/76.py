class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        m = arr[floor((len(arr)-1)/2)]
        res = []
        while len(res) < k:
            if abs(arr[-1] - m) >= abs(arr[0] - m):
                res.append(arr[-1])
                del arr[-1]
            else:
                res.append(arr[0])
                del arr[0]
        return res
