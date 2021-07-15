

class Job:
    def __init__(self, start_time, end_time, weight):
        self.start_time = start_time
        self.end_time = end_time
        self.weight = weight

    def __hash__(self):
        return hash((self.start_time, self.end_time, self.weight))

    def __eq__(self, other):
        return self.start_time == other.start_time and self.end_time == other.end_time and self.weight == other.weight


class WeightedIntervalSchedule:

    def __init__(self, sch):
        self.jobs = list()
        for job in sch:
            self.jobs.append(Job(job[0], job[1], job[2]))

        self.jobs_end_first = []
        self.jobs_start_first = []
        self.X = len(self.jobs) * [0]
        self.previous_job_mapping = dict()
        self.compute_latest_job_scheduled_before()
        self.memory = dict()
        

    def getResult(self):
        return self.dp(self.jobs_end_first, len(self.jobs) - 1, self.previous_job_mapping)

    def compute_latest_job_scheduled_before(self):

        self.jobs_start_first = sorted(self.jobs, key=lambda x: x.start_time)
        self.jobs_end_first = sorted(self.jobs, key=lambda x: x.end_time)

        self.X[0] = -1

        for i in range(1, len(self.jobs_start_first)):
            j = self.X[i - 1]
            while (self.jobs_start_first[i].start_time >= self.jobs_end_first[j + 1].end_time):
                j = j + 1

            self.X[i] = j
        
        for i in range(0, len(self.jobs_start_first)):
            self.previous_job_mapping[self.jobs_start_first[i]] = self.X[i]

        print((self.X))
            

    def dp(self, jobs, index, mapping):

        current_job = jobs[index]

        profit_including_current_job = current_job.weight
        profit_excluding_current_job = 0

        if index == 0:
            return profit_including_current_job

        if index in self.memory:
            return self.memory[index]

        if mapping[jobs[index]] != -1:
            profit_including_current_job += self.dp(
                jobs, mapping[jobs[index]], mapping)

        profit_excluding_current_job = self.dp(
            jobs, index - 1, mapping)

        result = max(profit_including_current_job, profit_excluding_current_job)
        self.memory[index] = result
        
        return result


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        temp = list()
        for i in range(len(startTime)):
            temp.append([startTime[i], endTime[i], profit[i]])
            
        return WeightedIntervalSchedule(temp).getResult()
        

