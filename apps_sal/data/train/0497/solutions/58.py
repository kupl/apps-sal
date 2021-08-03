class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        l = len(startTime)
        sep = list(zip(endTime, startTime, profit))
        # for i in range(l):
        #     sep.append(())
        sep = sorted(sep)
       # print(sep)
        dp = [0] * (sep[-1][0] + 1)
        j = 0
        for i in range(2, len(dp)):
            if sep[j][0] != i:
                dp[i] = dp[i - 1]
            else:
                dp[i] = max(dp[i - 1], sep[j][2] + dp[sep[j][1]])
                j += 1
                while (j < l and sep[j][0] == sep[j - 1][0]):
                    dp[i] = max(dp[i], sep[j][2] + dp[sep[j][1]])
                    j += 1
      #  print(dp)
        return dp[-1]
