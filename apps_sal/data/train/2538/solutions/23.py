class Solution:

    def countLargestGroup(self, n: int) -> int:
        dp = {0: 0}
        counter = [0] * 37
        for num in range(1, n + 1):
            (div, mod) = divmod(num, 10)
            dp[num] = dp[div] + mod
            counter[dp[num]] += 1
        return counter.count(max(counter))
