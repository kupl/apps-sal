class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans, cnt = 0, collections.Counter()
        for t in time:
            theOther = -t % 60
            ans += cnt[theOther]
            cnt[t % 60] += 1
        return ans
