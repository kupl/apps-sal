from functools import lru_cache


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = [(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))]
        jobs = sorted(jobs)

        @lru_cache(maxsize=None)
        def dp(i):
            if i >= len(jobs):
                return 0
            if i == len(jobs) - 1:
                return jobs[-1][2]
            l, r = i + 1, len(jobs) - 1
            j = l
            while l <= r:
                m = (l + r) // 2
                if jobs[m][0] < jobs[i][1]:
                    l = m + 1
                    j = max(j, m + 1)
                elif jobs[m][0] == jobs[i][1]:
                    r = m - 1
                    j = m
                else:
                    r = m - 1
                    j = m
            return max(jobs[i][2] + dp(j), dp(i + 1))

        return dp(0)
