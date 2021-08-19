class Solution:

    def countLargestGroup(self, n: int) -> int:
        dp = {0: 0}
        counts = [0] * 36
        for i in range(1, n + 1):
            (a, b) = divmod(i, 10)
            dp[i] = b + dp[a]
            counts[dp[i] - 1] += 1
        return counts.count(max(counts))
