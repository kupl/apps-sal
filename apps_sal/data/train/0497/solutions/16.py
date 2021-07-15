
class Solution:       
    def findPreviousJob(self, jobs, curIdx):
        low = 0
        high = curIdx - 1
        while (low < high):
            mid = low + (high-low+1)//2
            if jobs[mid].end <= jobs[curIdx].start:
                low = mid
            else:
                high = mid - 1
        return low

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        for i in range(len(profit)):
            job = Job(startTime[i], endTime[i], profit[i])
            jobs.append(job)
        jobs.sort(key=lambda x:x.end)
        # for job in jobs:
            # print(job.start, ', ', job.end, ', ', job.profit)
        dp = [0] * len(jobs)
        dp[0] = jobs[0].profit
        for i in range(1, len(jobs)):
            dp[i] = jobs[i].profit
            # find the job whose end time is smaller than job i's start time
            index = self.findPreviousJob(jobs, i)
            if jobs[index].end <= jobs[i].start:
                dp[i] += dp[index]
            '''
            index = -1
            for j in range(i):
                if jobs[j].end <= jobs[i].start:
                    index = j
                else:
                    break
            if index >= 0:
                dp[i] = dp[index] + dp[i]
            '''
            dp[i] = max(dp[i-1], dp[i])
            # print(dp)
        return dp[len(jobs)-1]
            
class Job:
    def __init__(self, start, end, profit):
        self.start = start
        self.end = end
        self.profit = profit

