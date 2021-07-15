class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Approach: dfs with memoization
        
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
        for i in range(index + 1, len(self.jobs)):
            if self.jobs[index][1] <= self.jobs[i][0]:
                return i
        return len(self.jobs)
