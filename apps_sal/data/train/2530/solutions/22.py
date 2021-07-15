class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnt = collections.Counter(t%60 for t in time)
        ans = cnt[0]*(cnt[0]-1)//2 + cnt[30]*(cnt[30]-1)//2
        for c in range(1,30):
            ans += cnt[c]*cnt[60-c]
        return ans
