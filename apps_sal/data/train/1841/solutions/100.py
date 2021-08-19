class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        res = []
        arr.sort()
        i = 0
        j = len(arr) - 1
        m = arr[(len(arr) - 1) // 2]
        while len(res) < k and i <= j:
            print(i)
            if m - arr[i] > arr[j] - m:
                res.append(arr[i])
                i += 1
            else:
                res.append(arr[j])
                j -= 1
        return res
