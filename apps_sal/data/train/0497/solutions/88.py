class Solution:

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        self.schedule = list(zip(startTime, endTime, profit))
        self.schedule.sort()
        self.scheduleLen = len(self.schedule)
        self.mem = [-1] * self.scheduleLen
        return self.getMaxProfit(0)

    def getMaxProfit(self, idx):
        if idx >= self.scheduleLen:
            return 0
        if self.mem[idx] != -1:
            return self.mem[idx]
        prof = 0
        endTime = self.schedule[idx][1]
        profit = self.schedule[idx][2]
        prof = max(prof, self.getMaxProfit(idx + 1))
        nextJob = self.getNextNonOverlappingJob(idx, endTime)
        prof = max(prof, profit + self.getMaxProfit(nextJob))
        self.mem[idx] = prof
        return self.mem[idx]

    def getNextNonOverlappingJob(self, i, endTime):
        while i < self.scheduleLen and self.schedule[i][0] < endTime:
            i += 1
        return i
