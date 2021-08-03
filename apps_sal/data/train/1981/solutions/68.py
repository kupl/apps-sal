class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        N = len(nums)
        C = [0] * (N + 1)

        for s, e in requests:
            C[s] += 1
            C[e + 1] -= 1

        for i in range(1, N):
            C[i] += C[i - 1]

        C.pop()

        perm = [0] * N
        csort = [i for i, _ in sorted([(i, c) for i, c in enumerate(C)], key=lambda x: x[1])]

        for i, n in zip(csort, sorted(nums)):
            perm[i] = n

        for i in range(1, N):
            perm[i] += perm[i - 1]

        result = 0
        for s, e in requests:
            if s == 0:
                result += perm[e]
            else:
                result += perm[e] - perm[s - 1]

        return result % (10 ** 9 + 7)
