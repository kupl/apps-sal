class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        
        # tps = sorted(zip(endTime,startTime, profit))
        # print (tps)
        # return 0
        events = []
        n = len(startTime)
        for i in range(n):
            events.append((startTime[i], i + 1))            
            events.append((endTime[i], -i - 1))
        
        events.sort()
        # print (events)
        
        p = 0
        for (curr, idx) in events:
            if idx > 0:
                profit[idx - 1] += p
            else:
                p = max(p, profit[-idx - 1])
            # print (curr, p)
        return p

