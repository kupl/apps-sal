class Solution:

    def longestAwesome(self, s: str) -> int:
        n = len(s)
        a = 0
        ans = 0
        dp = {0: -1}
        for i in range(n):
            a = a ^ 1 << int(s[i])
            if a in dp:
                ans = max(ans, i - dp[a])
            else:
                dp[a] = i
            for j in range(11):
                x = a ^ 1 << j
                if x in dp:
                    ans = max(ans, i - dp[x])
        return ans
