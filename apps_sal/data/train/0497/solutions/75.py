class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        slots = {}
        slots = set(startTime + endTime)
        time = {}

        c = 0
        for s in sorted(list(slots)):
            time[s] = c
            c += 1

        for i in range(len(startTime)):
            startTime[i] = time[startTime[i]]

        tasks = collections.defaultdict(list)
        for i in range(len(endTime)):
            endTime[i] = time[endTime[i]]
            tasks[endTime[i]].append(i)

        dp = [0] * c
        for t in range(0, c):
            dp[t] = dp[t - 1]
            for job in tasks[t]:
                st = startTime[job]
                dp[t] = max(dp[t], dp[st] + profit[job])

        return max(dp)
