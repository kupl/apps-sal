class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        lis = []
        dp = []
        for i in range(len(startTime)):
            lis += [[startTime[i], endTime[i], profit[i]]]
        lis = sorted(lis, key=lambda x: x[0])
        dp += [lis[-1][2]]
        for i in range(len(lis) - 2, -1, -1):
            cur = lis[i][2]
            for j in range(i + 1, len(lis)):
                if lis[j][0] >= lis[i][1]:

                    cur = lis[i][2] + dp[i - j]
                    break
            dp += [max(cur, dp[-1])]

        return dp[-1]
