
# This class represents a job = [start-time, end-time, weight]
class Job:
    def __init__(self, start_time, end_time, weight):
        self.start_time = start_time
        self.end_time = end_time
        self.weight = weight

    #overriding hashcode and equals to use the Job object as a key in dict
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
        self.previous_job = len(self.jobs) * [0]
        # Memoization will be done using this memory dict
        self.memory = dict()
        #computing the previous mappings
        self.compute_latest_job_scheduled_before()
        

    def getResult(self):
        return self.dp(self.jobs_end_first, len(self.jobs) - 1, self.previous_job)

    def compute_latest_job_scheduled_before(self):
        
        # Sorting the jobs in non decreasing order of end_time - O(nlogn)
        self.jobs_end_first = sorted(self.jobs, key=lambda x: x.end_time)

        indexed_jobs_start_first = [(index, job) for index, job in enumerate(self.jobs_end_first)]
        # Sorting the jobs in non decreasing order of start_time - O(nlogn)
        self.jobs_start_first = sorted(indexed_jobs_start_first, key=lambda x: x[1].start_time)

        # This list X will store the index of the previous job in jobs_end_first
        X = len(self.jobs) * [0]
        X[0] = -1

        # The time complexity of this method is O(n) as the statement inside the while loop
        # is only called once for each index
        # We use the intution that the latest job for the current job will be greater than or 
        # equal to the latest job for the preious job
        for i in range(1, len(self.jobs_start_first)):
            j = X[i - 1]
            while (self.jobs_start_first[i][1].start_time >= self.jobs_end_first[j + 1].end_time):
                j = j + 1

            X[i] = j

        # We now map the respective job to its index in jobs_end_first.
        # O(n)        
        for i in range(0, len(self.jobs_start_first)):
            self.previous_job[self.jobs_start_first[i][0]] = X[i]
            

    def dp(self, jobs, index, previous_job):

        dp = [0] * len(jobs)
        dp[0] = jobs[0].weight

        for i in range(1, len(jobs)):

            if (previous_job[i] != -1):
                dp[i] = max(dp[i - 1], jobs[i].weight + dp[previous_job[i]])
            else:
                dp[i] = max(jobs[i].weight, dp[i - 1])

        return dp[len(jobs) - 1]



class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        temp = list()
        for i in range(len(startTime)):
            temp.append([startTime[i], endTime[i], profit[i]])
            
        return WeightedIntervalSchedule(temp).getResult()
        

