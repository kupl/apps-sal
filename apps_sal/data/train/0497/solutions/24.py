class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        n = len(startTime)
        jobs = []
        for i in range(n):
            jobs.append((startTime[i], endTime[i], profit[i]))

        jobs.sort(key=lambda x: (x[1], x[0], x[2]))

        from sortedcontainers import SortedDict
        sd = SortedDict()

        result = 0

        for i in range(n):
            start, end, profit = jobs[i]
            previ = sd.bisect_right(start)
            if previ == 0:
                sd[end] = max(result, profit)
            else:
                prev_key = list(sd.keys())[previ - 1]
                sd[end] = max(result, profit + sd.get(prev_key))

            result = max(result, sd.get(end))

        # print(sd)
        return result
