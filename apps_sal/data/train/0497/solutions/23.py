class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

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
        jobs.sort(key=lambda x: x[1])
        dp = [[0, 0]]
        for job in jobs:
            maxLast = bs(dp, job[0])[1]
            if maxLast + job[2] > dp[-1][1]:
                dp.append([job[1], maxLast + job[2]])
        return dp[-1][1]
