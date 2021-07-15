class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        
        hel = [[startTime[i], 1, endTime[i], profit[i]] for i in range(len(startTime))]
        heapq.heapify(hel)
        res = 0
        
        while hel:
            
            ele = heapq.heappop(hel)
             
            if ele[1] == 1:
                heapq.heappush(hel, [ele[2], 0, ele[2], ele[-1]+res])
                
            else:
                res = max(res,ele[-1])
                
        return res

