class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        line=list(set(startTime)|set(endTime))
        line.sort()
        dp=dict()
        d=dict()
        v=dict()
        for i in range(len(endTime)):
            if endTime[i] not in d:
                d[endTime[i]]=[]
            d[endTime[i]].append(startTime[i])
            v[(startTime[i],endTime[i])]=profit[i]
        m=0
        for n in line:
            if n not in d:
                dp[n]=m
            else:
                dp[n]=max([m]+[dp[i]+v[(i,n)]  for i in d[n]])
                m=max(dp[n],m)
        return dp[line[-1]]
