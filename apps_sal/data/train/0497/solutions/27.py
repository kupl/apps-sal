class JOB:

    def __init__(self, start, end, profit):
        self.start = start
        self.end = end
        self.profit = profit


class Solution:

    def binsearch(self, job, start_index):
        lo = 0
        hi = start_index - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if job[mid].end <= job[start_index].start:
                if job[mid + 1].end <= job[start_index].start:
                    lo = mid + 1
                else:
                    return mid
            else:
                hi = mid - 1
        return -1

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        job = []
        n = len(profit)
        for i in range(n):
            job.append(JOB(startTime[i], endTime[i], profit[i]))
        job = sorted(job, key=lambda x: x.end)
        table = [0 for i in range(n)]
        table[0] = job[0].profit
        for i in range(1, len(profit)):
            cur_profit = job[i].profit
            l = self.binsearch(job, i)
            if l != -1:
                cur_profit += table[l]
            table[i] = max(table[i - 1], cur_profit)
        return table[-1]
