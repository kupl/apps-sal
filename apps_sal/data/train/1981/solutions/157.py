class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        r = 10**5+1
        f = [0]*r
        for s, e in requests:
            f[s] += 1
            f[e+1] -= 1
        freq = {}
        curr = 0
        for i in range(r):
            curr += f[i]
            if curr != 0:
                freq[curr] = freq.get(curr, 0) + 1
        sol = 0
        nums.sort()
        for k, v in sorted([(k, v) for k, v in freq.items()], reverse=True):
            for _ in range(v):
                sol += k*nums.pop()
        return sol % (10**9 + 7)
