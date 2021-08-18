class Solution:
    def findprofit(self, arr):
        dp = [0 for i in range(len(arr))]
        dp[0] = arr[0][2]

        for i in range(1, len(dp)):
            including = arr[i][2]

            last_non_conflict_job = -1
            for j in range(i - 1, -1, -1):
                if arr[j][1] <= arr[i][0]:

                    last_non_conflict_job = j
                    break

            if last_non_conflict_job != -1:
                including += dp[last_non_conflict_job]

            dp[i] = max(dp[i - 1], including)
        return(dp[-1])

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        arr = list(zip(startTime, endTime, profit))
        arr.sort(key=lambda x: x[1])

        return(self.findprofit(arr))
