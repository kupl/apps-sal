class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n=len(profit)
        schedule=[(startTime[i],endTime[i],profit[i]) for i in range(len(startTime))]
        schedule.sort(key=lambda x:(x[1]))
        dp=[0]*(n+1)
        dp[0]=0
        p=[0]*(n+1)
        value=[]
        value.append(0)              
        for i in range(n):
             value.append(schedule[i][2])
        bs=[]
        bs.append(schedule[0][1])
        p[1]=0
        def bst(bs,x):
            h=len(bs)-1
            l=0
            while(l<=h):
                m=(l+h)//2
                if bs[m]==x:
                      return m+1
                elif bs[m]<x:
                      l=m+1
                else:
                      h=m-1 
            return l
        for i in range(2,n+1):
                p[i]=bst(bs,schedule[i-1][0])
                bs.append(schedule[i-1][1])
        for i in range(1,n+1):
                    dp[i]=max(dp[i-1],dp[p[i]]+value[i])
        return dp[-1]

