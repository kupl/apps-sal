class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        seen = collections.Counter()
        ans = 0
        for t in time:
            ans += seen[-t % 60]
            seen[t % 60] += 1
        return ans
