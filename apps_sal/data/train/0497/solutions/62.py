class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(profit)
        timeline = []
        for i in range(n): 
            timeline.append((startTime[i], n)), 
            timeline.append((endTime[i], i))
            
        mapping = {}
        dp = [0] * (2 * n)
        for i, v in enumerate(sorted(timeline)):
            if v[1] < n:
                dp[i] = max(dp[i - 1], dp[mapping[startTime[v[1]]]] + profit[v[1]])
            else:
                dp[i] = dp[i - 1];
                mapping[v[0]] = i
                
        return dp[-1]
