class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        sarr = sorted(arr)
        L = len(arr)
        if L / 2 % 1 == 0:
            median = sarr[int((L - 1) / 2)]
        else:
            median = sarr[int(L / 2 - 0.5)]
        tarr = [[abs(arr[i] - median), arr[i]] for i in range(L)]
        tarr = sorted(tarr, reverse=True)
        res = [tarr[i][1] for i in range(L) if i < k]
        return res
