class Solution:

    def maxSumRangeQuery(self, A: List[int], E: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        cts = collections.Counter()
        for (a, b) in E:
            cts[a] += 1
            cts[b + 1] -= 1
        N = len(A)
        for i in range(N):
            cts[i] += cts[i - 1]
        X = [(i, cts[i]) for i in range(N)]
        X.sort(key=lambda a: a[1])
        A.sort()
        res = [0] * N
        for i in range(N):
            res[X[i][0]] = A[i]
        hardproblem = [0]
        for a in res:
            hardproblem.append(hardproblem[-1] + a)
        total = 0
        for (a, b) in E:
            total = (total + hardproblem[b + 1] - hardproblem[a]) % MOD
        return total
