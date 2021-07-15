# https://leetcode.com/problems/count-all-possible-routes/discuss/843602/Java-or-DP-all-approaches --> another dp solution
class Solution:
    def countRoutes(self, a: List[int], s: int, e: int, f: int) -> int:
        ans, n = 0, len(a)
        dp = [[0]*(f+1) for _ in range(n)]
        dp[s][0] = 1
        for ff in range(f+1):
            for i in range(n):
                for k in range(n):
                    if i != k:
                        dist = abs(a[i] - a[k])
                        if dist <= ff: dp[i][ff] += dp[k][ff-dist]
            ans += dp[e][ff]
        return ans % (10**9+7)
