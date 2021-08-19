class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        N = len(arr)
        median = arr[(N - 1) // 2]
        lp = 0
        rp = N - 1
        output = []
        for i in range(k):
            lps = abs(arr[lp] - median)
            rps = abs(arr[rp] - median)
            if rps >= lps:
                output.append(arr[rp])
                rp -= 1
                continue
            else:
                output.append(arr[lp])
                lp += 1
        return output
