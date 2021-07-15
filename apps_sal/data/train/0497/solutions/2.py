class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # TLE
        # jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        # dp = defaultdict(int)
        # dp[0] = 0
        # #find the max profit before time i
        # def find(i):
        #     tmp = []
        #     for time in dp:
        #         if time<=i:
        #             tmp.append(dp[time])
        #     return max(tmp)
        # for s, e, p in jobs:
        #     dp[e] = max(find(e),find(s)+p)
        # return max(list(dp.values()))
        
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        # time 0: profit 0
        dp = [(0,0)]
        
        #find the max profit before time i
        def find(time):
            size = len(dp)
            for i in range(size-1,-1,-1):
                pre_time = dp[i][0]
                if pre_time<=time:
                    return dp[i][1]
            
        for s, e, p in jobs:
            dp.append((e,max(find(e),find(s)+p)))
            
        return dp[-1][1]


