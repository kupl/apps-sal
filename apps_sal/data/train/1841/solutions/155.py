class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        res = []
        median = arr[(n - 1) // 2]
        l = []
        arr.reverse()
        for i in range(n):
            l.append([arr[i], abs(median - arr[i])])
        l.sort(reverse=True, key=lambda x: x[1])
        i = 0
        while i < k - 1 or (i < n - 1 and l[i][1] == l[i + 1][1]):
            res.append(l[i][0])
            i += 1
        res.append(l[i][0])
        return res[:k]
