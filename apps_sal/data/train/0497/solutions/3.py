class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        dp = [0]*(len(profit))
        intervals = [(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))]
        intervals.sort(key=lambda x: x[1])
        dp[0] = intervals[0][2]
        for j in range(1, len(dp)):
            dp[j]=max(intervals[j][2], dp[j-1])
            l=0;r=len(intervals)-1
            while(l<r):
                mid=l+((r-l+1)>>1)
                if(intervals[mid][1]<=intervals[j][0]):
                    l=mid
                else:
                    r=mid-1
            if(intervals[j][0]>=intervals[l][1]):
                dp[j]=max(dp[j], intervals[j][2]+dp[l])
        return dp[-1]
