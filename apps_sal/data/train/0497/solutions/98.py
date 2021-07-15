class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        def bs(list1, target):
            left = 0
            right = len(list1) - 1
            while left < right - 1:
                mid = (left + right) // 2
                if list1[mid][1] == target:
                    return list1[mid]
                elif list1[mid][1] < target:
                    left =  mid
                else:
                    right = mid - 1
            if list1[right][1] <= target:
                return list1[right]
            else:
                return list1[left]
        
        
        jobs = []
        for i in range(len(startTime)):
            jobs.append([startTime[i], endTime[i], profit[i]])
        dp = [[0, 0, 0]]
        
        lastMax = 0
        
        jobs.sort(key = lambda x:x[1])
        for job in jobs:
            lastMax = dp[-1][2]
            candidate = bs(dp, job[0])
            if candidate[2] + job[2] > lastMax:
                
                dp.append([job[0], job[1], candidate[2] + job[2]])
        print(dp)
        return dp[-1][-1]
        

