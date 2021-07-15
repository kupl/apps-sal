class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = []
        n = len(startTime)
        for i in range(n):
            intervals.append((startTime[i], endTime[i], profit[i]))

        intervals.sort(key = lambda x:x[1]) # sorted by endTime
        T = intervals[-1][1] # largest time

        dp = [0] *(T + 1)
        co = [0] *(T + 1)
        for i in range(n):
            s, e, p = intervals[i] 
            if dp[s]+p > dp[e]:
                dp[e] = dp[s]+p
                co[e] = co[s]+1
            if i == n - 1: break
            nxte = intervals[i+1][1] + 1      
            for t in range(e + 1, nxte):
                dp[t] = dp[e]
                co[t] = co[e]
        print(co[T])
        return dp[T]
