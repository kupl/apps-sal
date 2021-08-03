class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        for i in range(len(startTime)):
            jobs.append([endTime[i], startTime[i], profit[i]])
        jobs.sort()
        # print(jobs)
        dp = [0] * (max(endTime) + 1)
        arr = [0]
        for job in jobs:
            prev_largest_idx = self.get_prev_idx(job[1], arr)
            curr_max = max(job[2] + dp[prev_largest_idx], dp[arr[-1]])
            dp[job[0]] = max(curr_max, dp[job[0]])
            arr.append(job[0])
        # print(dp)
        return dp[-1]

    def get_prev_idx(self, target, arr):
        # find the greatest number smaller or equal to target in sorted arr
        # print('---')
        # print(target)
        # print(arr)
        if arr[-1] <= target:
            return arr[-1]
        l, r = 0, len(arr) - 1
        while l < r:
            mid = l + (r - l) // 2
            if arr[mid] > target:
                r = mid
            else:
                l = mid + 1
        # if arr[l] <= target:
        #     # print(arr[l])
        #     return arr[l]
        # print(arr[l-1])
        return arr[l - 1]
