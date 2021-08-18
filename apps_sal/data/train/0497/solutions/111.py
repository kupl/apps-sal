class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        self.jobs = list()

        for i in range(len(startTime)):
            self.jobs.append((startTime[i], endTime[i], profit[i]))

        self.jobs.sort()
        self.memo = dict()
        return self.dfs(0)

    def dfs(self, index):
        if index == len(self.jobs):
            return 0
        if index in self.memo:
            return self.memo[index]

        res = 0

        res = max(res, self.dfs(index + 1))

        nextIndex = self.findNext(index)
        res = max(res, self.dfs(nextIndex) + self.jobs[index][2])
        self.memo[index] = res

        return res

    def findNext(self, index):
        left = index + 1
        right = len(self.jobs)
        target = self.jobs[index][1]
        while left < right:
            mid = (left + right) // 2
            if self.jobs[mid][0] < target:
                left = mid + 1
            else:
                right = mid
        return left
