class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        # K * n
        temp = list(arr)
        temp.sort()
        median = 0

        median = temp[(len(temp) - 1) // 2]

        l = 0
        r = len(arr) - 1
        res = []
        while k > 0:
            if median - temp[l] <= temp[r] - median:
                res.append(temp[r])
                r -= 1
            else:
                res.append(temp[l])
                l += 1
            k -= 1
        return res
