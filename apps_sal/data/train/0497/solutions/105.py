class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])

        def search(idx):
            e_time = jobs[idx][0]
            l, r = 0, idx - 1
            while l <= r:
                mid = (r - l) // 2 + l
                if jobs[mid][1] <= e_time:
                    if jobs[mid + 1][1] <= e_time:
                        l = mid + 1
                    else:
                        return mid
                else:
                    r = mid - 1
            return -1

        def find(idx):
            e_time = jobs[idx][0]
            l, r = 0, idx
            while l < r:
                mid = (r - l) // 2 + l
                if jobs[mid][1] <= e_time:
                    l = mid + 1
                else:
                    r = mid
            return l - 1

        dp = [0] * len(jobs)
        dp[0] = jobs[0][2]

        for i in range(1, len(jobs)):
            profit = jobs[i][2]
            j = find(i)
            if j != -1:
                profit += dp[j]
            dp[i] = max(dp[i - 1], profit)

        print(dp)
        return dp[-1]
