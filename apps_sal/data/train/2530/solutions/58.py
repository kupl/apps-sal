class Solution:

    def numPairsDivisibleBy60(self, times: List[int]) -> int:
        remain = [0 for i in range(60)]
        ans = 0
        for time in times:
            ans += remain[-time % 60]
            remain[time % 60] += 1
        return ans
