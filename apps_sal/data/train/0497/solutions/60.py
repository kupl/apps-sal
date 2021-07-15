class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobLen = len(startTime)
        jobSchedule = []
        for s, e, p in zip(startTime, endTime, profit):
            jobSchedule.append((s, e, p))
        jobSchedule.sort(key = lambda x:(x[0], x[1], -x[2]))
        
        # print(jobSchedule)
        
        dp = {}
        
        def findNextJob(preE, preI):
            
            l = preI
            r = jobLen - 1
            if preE > jobSchedule[r][0]:
                return 0
            
            if (preE, preI) in dp:
                return dp[(preE, preI)]
            
            while r > l:
                m = (r + l) // 2
                if jobSchedule[m][0] < preE:
                    l = m + 1
                else:
                    r = m
            lastStart = jobSchedule[l][1]
            bestP = 0
            bestE = 0
            subAns = 0
            for nextJob in range(l, jobLen):
                if jobSchedule[nextJob][0] >= lastStart:
                    break
                if jobSchedule[nextJob][1] >= bestE and jobSchedule[nextJob][2] <= bestP:
                    continue
                if jobSchedule[nextJob][2] > bestP or (jobSchedule[nextJob][2] == bestP and jobSchedule[nextJob][1] < bestE):
                    bestP = jobSchedule[nextJob][2]
                    bestE = jobSchedule[nextJob][1]
                subAns = max(subAns, jobSchedule[nextJob][2] + findNextJob(jobSchedule[nextJob][1], nextJob))
            dp[(preE, preI)] = subAns
            return subAns
    
        return findNextJob(0, 0)

