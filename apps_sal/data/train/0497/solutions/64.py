class Solution:
    # DP bottom-up working from end to start
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        arr, length = [], len(startTime)
        for i in range(length):
            arr.append([startTime[i], endTime[i], profit[i]])
        arr.sort()

        ans = arr[-1][2]
        max_start, max_prof, dp = arr[-1][0], arr[-1][2], {}
        dp[arr[-1][0]] = arr[-1][2]
        for i in range(length - 2, -1, -1):
            start, end, prof = arr[i]
            after = 0
            while end <= max_start:
                if end in dp:
                    after = dp[end]
                    break
                end += 1

            dp[start] = max(max_prof, prof + after)
            ans, max_prof = dp[start], dp[start]
        return ans
