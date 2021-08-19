class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        for i in range(len(startTime)):
            jobs.append([startTime[i], endTime[i], profit[i]])

        jobs = sorted(jobs, key=lambda x: x[1])
        dp = [0 for i in range(len(jobs))]
        dp[0] = jobs[0][2]

        def search(target):
            # larger than or equal to target
            l, r = 0, len(jobs)
            while l < r:
                mid = l + (r - l) // 2
                if jobs[mid][1] < target:
                    l = mid + 1
                else:
                    r = mid

            return l

        # print(jobs)

        for i in range(1, len(jobs)):
            start, end, profit = jobs[i]
            # search for previous jobs ends before current job
            idx = search(start)
            if jobs[idx][1] == start:
                prev_best = dp[idx]
            elif jobs[idx - 1][1] < start:
                prev_best = dp[idx - 1]
            else:
                prev_best = 0

            # print(start, idx, jobs[idx][1], prev_best)

            dp[i] = max(dp[i - 1], profit + prev_best)

            # print(dp)

        return dp[-1]
