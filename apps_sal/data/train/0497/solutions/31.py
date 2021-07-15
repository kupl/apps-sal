class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        dp = [0 for _ in range(len(startTime))]
        
        intervals = [(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))]
        
        intervals.sort()
        
        def findNext(curr):
            for n in range(curr+1, len(intervals)):
                if intervals[n][0] >= intervals[curr][1]:
                    return n
            return -1
            
        for i in range(len(intervals)-1, -1, -1):
            currS, currE, currP = intervals[i]
            
            nextI = findNext(i)
            dp[i] = max(currP + (0 if nextI == -1 else dp[nextI]), 0 if i == len(intervals)-1 else dp[i+1])


                
        return max(dp)

