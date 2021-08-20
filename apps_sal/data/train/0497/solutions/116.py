class Solution:

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        for (s, e, p) in zip(startTime, endTime, profit):
            jobs.append([s, e, p])
        jobs.sort(key=lambda x: x[0])
        memo = [0] * len(jobs)

        def recur(i):
            if i >= len(jobs):
                return 0
            if memo[i] > 0:
                return memo[i]
            else:
                pro = 0
                (l, r) = (i + 1, len(jobs))
                while l < r:
                    mid = (l + r) // 2
                    if jobs[mid][0] < jobs[i][1]:
                        l = mid + 1
                    else:
                        r = mid
                pro = max(recur(i + 1), recur(l) + jobs[i][2])
                memo[i] = pro
                return pro
        return recur(0)
