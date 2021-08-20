class Solution:

    def maxSumRangeQuery(self, A, qs):
        A.sort(reverse=1)
        n = len(A)
        r = [0] * (n + 1)
        for (a, b) in qs:
            r[a] += 1
            r[b + 1] -= 1
        for i in range(1, n):
            r[i] += r[i - 1]
        r.pop()
        r.sort(reverse=1)
        ans = 0
        for (i, k) in enumerate(r):
            ans += A[i] * k
        return ans % (10 ** 9 + 7)
