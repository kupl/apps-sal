class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = list(zip(endTime, startTime, profit))
        jobs.sort()

        def binary_search(jobs, i):
            left = 0
            right = i - 1
            while left <= right:
                mid = (left + right) // 2
                if jobs[mid][0] <= jobs[i][1]:
                    if jobs[mid + 1][0] <= jobs[i][1]:
                        left = mid + 1
                    else:
                        return mid
                else:
                    right = mid - 1
            return -1

        dp = [0] * n
        dp[0] = jobs[0][2]
        for i in range(1, n):
            k = binary_search(jobs, i)
            if k != -1:
                dp[i] = max(dp[k] + jobs[i][2], dp[i - 1])
            else:
                dp[i] = max(jobs[i][2], dp[i - 1])
        return dp[n - 1]
