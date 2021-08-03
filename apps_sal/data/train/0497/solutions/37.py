class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))

        memo = {}

        def maximize_profit(start_time, min_job_id):
            if start_time in memo:
                return memo[start_time]

            i = min_job_id
            while i < len(jobs) and jobs[i][0] < start_time:
                i += 1

            max_profit = 0
            min_end_time = float('inf')
            while i < len(jobs) and jobs[i][0] < min_end_time:
                profit = jobs[i][2] + maximize_profit(jobs[i][1], i + 1)
                max_profit = max(max_profit, profit)
                min_end_time = min(min_end_time, jobs[i][1])
                i += 1

            memo[start_time] = max_profit
            return max_profit

        return maximize_profit(0, 0)
