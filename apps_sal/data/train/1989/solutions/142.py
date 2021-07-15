class Solution:
    def longestAwesome(self, s: str) -> int:
        earliest_occ = defaultdict(lambda: float('inf'))
        earliest_occ[0] = -1
        msk = 0
        ans = 1
        for i in range(len(s)):
            msk ^= (1<<int(s[i]))
            earliest_occ[msk] = min(i, earliest_occ[msk])
            for j in range(10):
                ans = max(ans, i - earliest_occ[msk^(1<<j)])
            ans = max(ans, i - earliest_occ[msk])
        return ans

