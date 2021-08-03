class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Approach: dfs with memoization
        # after bundling start time, end time together and sort

        self.jobs = list()

        # bundle start time, end time and profit together
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

        # the case when we don't do the job
        res = max(res, self.dfs(index + 1))

        # use binary search to find the next index if we decide to do this job
        nextIndex = self.findNext(index)
        res = max(res, self.dfs(nextIndex) + self.jobs[index][2])
        self.memo[index] = res

        return res

    # Binary search to find the next index
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
