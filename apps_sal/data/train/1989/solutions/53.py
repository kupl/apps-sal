class Solution:
    def longestAwesome(self, s: str) -> int:
        dp = {} # 表示每个state的最小下表
        dp[0] = -1
        state, ans = 0, 0
        for i, c in enumerate(s):
            state ^= (1<<int(c))
            if state not in dp: dp[state] = i
            else:
                # 当前state和之前的某一个state完成全同时
                ans = max(ans, i - dp[state])
            
            # 当前state和之前的某一个state只差一个bit时
            for num in range(10):
                if state ^ (1 << num) in dp:
                    ans = max(ans, i - dp[state ^ (1 << num)])
        
        return ans
