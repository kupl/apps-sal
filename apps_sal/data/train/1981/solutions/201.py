class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        starts = list(sorted([s for s, _ in requests]))
        ends = list(sorted([e for _, e in requests]))

        r = 0

        counts = []
        cur = 0
        si, ei = 0, 0
        for i in range(len(nums)):
            while si < len(starts) and starts[si] <= i:
                cur += 1
                si += 1
            while ei < len(ends) and ends[ei] < i:
                cur -= 1
                ei += 1
            counts.append(cur)

        sc = list(sorted(counts))
        sn = list(sorted(nums))

        # print(sc)
        # print(sn)

        for i in range(len(sc)):
            r += sc[i] * sn[i]

        return r % MOD
