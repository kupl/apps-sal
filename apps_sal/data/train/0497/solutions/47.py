class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        def find(i):
            l = -1
            r = i - 1
            while l < r:
                m = (l + r + 1) // 2
                if jobs[m][1] <= jobs[i][0]:
                    l = m
                else:
                    r = m - 1
            return l
        n = len(startTime)
        jobs = []
        for i in range(n):
            jobs.append([startTime[i], endTime[i], profit[i]])
        jobs.sort(key=lambda x: x[1])
        tot = [0 for _ in range(n + 1)]
        tot[0] = jobs[0][2]
        print(jobs)
        for i in range(1, n):
            p = find(i)
            tot[i] = max(tot[i - 1], tot[p] + jobs[i][2])
        return tot[n - 1]
