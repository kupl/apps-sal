class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        #用空间存在startTime开始前最大的profit
        #像找零钱一样写的话，会很慢
#         jobs = []
#         for i in range(len(startTime)):
#             jobs.append([startTime[i], endTime[i], profit[i]])
#         jobs.sort(key = lambda x:x[1])
        
#         dict1 = {}
#         for job in jobs:
#             if job[1] not in dict1:
#                 dict1[job[1]] = [job]
#             else:
#                 dict1[job[1]].append(job)
#         tail = jobs[-1][1]
#         dp = [0 for _ in range(tail + 1)]
        
#         for i in range(1, len(dp)):
#             dp[i] = dp[i-1]
#             if i in dict1:
#                 for job in dict1[i]:
#                     startTime = job[0]
#                     dp[i] = max(dp[i], dp[startTime] + job[2])
#         #print(dp)
#         return dp[-1]

        #因为仅有做决定的点有用，所以我们不需要把所有的点取下来，仅需要存每次做决定产生的最大值
        #就像找零钱，每次做决定的时候，找dp[cur - value]
        #但是因为我们只存了稀疏的链表结构，需要在存的结果中找那个对应的dp[cur - value]的点
        
        def bs(list1, target):
            left = 0
            right = len(list1) - 1
            while left < right - 1:
                mid = (left + right) // 2
                if target == list1[mid][0]:
                    return list1[mid]
                elif target > list1[mid][0]:
                    left = mid
                else:
                    right = mid - 1
            if list1[right][0] > target:
                return list1[left]
            else:
                return list1[right]
            
        jobs = []
        for i in range(len(startTime)):
            jobs.append([startTime[i], endTime[i], profit[i]])
        jobs.sort(key = lambda x:x[1])
        dp = [[0, 0]]
        for job in jobs:
            maxLast = bs(dp, job[0])[1]
            if maxLast + job[2] > dp[-1][1]:
                dp.append([job[1], maxLast + job[2]])
        return dp[-1][1]
            
        

