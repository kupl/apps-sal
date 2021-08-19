class Solution:
    def findprofit(self, arr):
        dp = [0 for i in range(len(arr))]
        dp[0] = arr[0][2]  # dp[i] -> profit till ith job (we know jobs are sorted by finish time)

        # now we start filling dp from index 1, cause 0 has been taken care of
        for i in range(1, len(dp)):
            including = arr[i][2]  # if we decide to include ith job's profit , we have to do some checks

            last_non_conflict_job = -1
            for j in range(i - 1, -1, -1):  # check all the previous jobs and find the one that doesnt conflict with this current ith job, we traverse in reverse to find the last one that doesnt conflict
                if arr[j][1] <= arr[i][0]:  # if end time of jth(previous ones) is less that start time of current ,, then we are good to go

                    last_non_conflict_job = j  # we found the job
                    break  # breaking here is very important otherwise we will not find the last job but the first job

            if last_non_conflict_job != -1:  # that means we know the previous job and we can now add our current job in it
                including += dp[last_non_conflict_job]

            dp[i] = max(dp[i - 1], including)  # dp[i] has two options, to take ith job or to not take ith job, we do whichever is maximum
        return(dp[-1])

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # arr = [[startTime[i],endTime[i],profit[i]] for i in range(len(startTime))]
        arr = list(zip(startTime, endTime, profit))
        arr.sort(key=lambda x: x[1])  # sort by finish time

        return(self.findprofit(arr))
