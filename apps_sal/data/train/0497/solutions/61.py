class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        n = max(endTime)
        dp, dicti = (n+2) * [0], collections.defaultdict(list)
        for start, end, profit in zip(startTime, endTime, profit):
            dicti[start].append([end, profit])
        
        for start in range(n, -1, -1):
            dp[start] = dp[start+1]
            
            if start in dicti:
                dp[start] = dp[start+1]
                for end, profit in dicti[start]:
                    dp[start] = max(dp[start], profit + dp[end])
        return dp[1]
