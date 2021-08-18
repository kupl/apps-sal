class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = list(zip(startTime, endTime, profit))
        jobs = sorted(jobs, key=lambda x: x[1])
        dp = [0] + profit

        def search_start(i):
            nonlocal jobs
            target = jobs[i][0]

            l, r = 0, i
            while l < r:
                mid = (l + r) // 2
                if jobs[mid][1] > target:
                    r = mid
                else:
                    l = mid + 1
            return l

        for i, (start_time, end_time, pft) in enumerate(jobs):
            pft_if_not_take_job = dp[search_start(i)]

            dp[i + 1] = max(dp[i], pft_if_not_take_job + pft)

        return dp[-1]
