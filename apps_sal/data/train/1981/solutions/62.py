class Solution:
    def maxSumRangeQuery(self, ar: List[int], requests: List[List[int]]) -> int:
        n = len(ar)
        pref = [0 for i in range(n)]
        for i in requests:
            pref[i[0]] += 1
            if i[1] + 1 < n:
                pref[i[1] + 1] -= 1
        for i in range(1, n):
            pref[i] = pref[i - 1] + pref[i]
        ar.sort(reverse=True)
        pref.sort(reverse=True)
        res = 0
        mod = (10**9) + 7
        for i, j in zip(ar, pref):
            res = (res + (i * j)) % mod
        return res
