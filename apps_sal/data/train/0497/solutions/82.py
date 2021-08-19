class Solution:

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted([[startTime[i], endTime[i], profit[i]] for i in range(len(startTime))])
        mem = {}
        return self.scheduleJobs(jobs, 0, mem)

    def scheduleJobs(self, jobs, i, mem):
        """
        select current job, and push i after the end time of jobs[i]
        or
        skip current job, and push i += 1
        """
        if i >= len(jobs):
            return 0
        if i in mem:
            return mem[i]
        profit1 = self.scheduleJobs(jobs, i + 1, mem)
        j = i + 1
        while j < len(jobs) and jobs[j][0] < jobs[i][1]:
            j += 1
        profit2 = self.scheduleJobs(jobs, j, mem) + jobs[i][2]
        mem[i] = max(profit1, profit2)
        return mem[i]
