class Solution:
    def maxSumRangeQuery(self, A: List[int], E: List[List[int]]) -> int:
        MOD = 10**9 + 7
        cts = collections.Counter()
        for a,b in E:
            cts[a] += 1
            cts[b+1] -= 1
        N = len(A)
        for i in range(N):
            cts[i] += cts[i-1]
        freqMap = [(i, cts[i]) for i in range(N)]
        freqMap.sort(key = lambda a: a[1])
        A.sort()
        res = [0]*N
        for i in range(N):
            res[freqMap[i][0]] = A[i]
        psum = [0]
        for a in res:
            psum.append(psum[-1] + a)
        total = 0
        for a,b in E:
            total = ( total + psum[b+1] - psum[a]) % MOD
        return total
