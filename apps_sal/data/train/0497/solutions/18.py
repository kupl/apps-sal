class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        '''
            take timeslot list: [(s1,f1)...(si, fi)]
            sort by finish time, build dp array
            dp[0] = 0
            dp[i] = max(take i, dont take i)
                  = max(first non overlapping j -> dp[j] + profit[i], dp[i-1]) 

            startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]


            timeslots [(0, 1, 3) (1, 2, 4) (2, 3, 5) (3, 3, 6)]
            dp [0, 50, 50, 90, 120]

        '''
        def bisect(arr, num, l, r):
            if l >= r:
                return l
            mid = (l + r + 1) // 2
            if arr[mid][2] > num:
                return bisect(arr, num, l, mid - 1)
            else:
                return bisect(arr, num, mid, r)

        n = len(startTime)
        timeslots = [(profit[i], startTime[i], endTime[i]) for i in range(n)]
        timeslots = sorted(timeslots, key=lambda a: a[2])
        dp = [0] * (n + 1)
        for i, (p, s, e) in enumerate(timeslots):
            j = bisect(timeslots, s, -1, n - 1) + 1
            dp[i + 1] = max(dp[j] + p, dp[i])

        return dp[-1]
