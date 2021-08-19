class Solution:

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        seen = {i: 0 for i in range(60)}
        for x in time:
            nextDiff = -x % 60
            curDiff = x % 60
            ans += seen[curDiff]
            seen[nextDiff] += 1
        return ans
