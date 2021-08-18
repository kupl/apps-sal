class Solution:
    def maxSumRangeQuery(self, a: List[int], b: List[List[int]]) -> int:
        n = len(a)
        p = [0] * (n + 1)
        for x in b:
            p[x[0]] += 1
            p[x[1] + 1] -= 1
        pref = [0] * n
        pref[0] = p[0]
        for i in range(1, n):
            pref[i] = p[i] + pref[i - 1]
        pref.sort(reverse=True)
        a.sort(reverse=True)
        s = 0
        for i in range(n):
            s += pref[i] * a[i]
        return s % (10**9 + 7)
