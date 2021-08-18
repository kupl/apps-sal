from sortedcontainers import SortedList


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        for i in range(len(startTime)):
            s = startTime[i]
            e = endTime[i]
            p = profit[i]
            jobs.append((e, s, p))

        jobs = sorted(jobs)
        jobs = SortedList(jobs)

        N = len(jobs)
        dp = [0 for _ in range(N)]

        dp[0] = jobs[0][2]

        for i in range(1, N):
            job = jobs[i]
            end_to_look = job[1]

            to_look_index = jobs.bisect_right((end_to_look, sys.maxsize, sys.maxsize))
            print(to_look_index)
            dp[i] = dp[i - 1]
            if to_look_index - 1 >= 0 and jobs[to_look_index - 1][0] <= job[1]:
                dp[i] = max(dp[i], dp[to_look_index - 1] + job[2])
            else:
                dp[i] = max(job[2], dp[i])

        return dp[N - 1]
