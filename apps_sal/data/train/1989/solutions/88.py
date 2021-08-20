from collections import defaultdict


class Solution:

    def longestAwesome(self, s: str) -> int:
        dlist = [1] * 10
        for i in range(9):
            dlist[i + 1] = dlist[i] * 2
        count = defaultdict(int)
        dp = dict()
        ans = 0
        dp[0] = -1
        for (i, num) in enumerate(s):
            count[num] += 1
            cur = 0
            curdp = 10 * [0]
            for ar in range(10):
                st = str(ar)
                val = count[st] % 2
                cur += val * dlist[ar]
                curdp[ar] = val
            if cur in dp:
                ans = max(ans, i - dp[cur])
            else:
                dp[cur] = i
            for ar in range(10):
                if curdp[ar] == 1:
                    val = -1
                else:
                    val = 1
                cur += val * dlist[ar]
                if cur in dp:
                    ans = max(ans, i - dp[cur])
                cur -= val * dlist[ar]
        return ans
