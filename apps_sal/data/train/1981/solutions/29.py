class Solution:

    def maxSumRangeQuery(self, A, req):
        n = len(A)
        count = [0] * (n + 1)
        for (i, j) in req:
            count[i] += 1
            count[j + 1] -= 1
        count = list(accumulate(count))[:-1]
        count.sort()
        A.sort()
        return sum([count[i] * A[i] for i in range(n)]) % (10 ** 9 + 7)
