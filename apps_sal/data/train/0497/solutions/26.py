class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        for i in range(len(startTime)):
            jobs.append([endTime[i], startTime[i], profit[i]])
        jobs.sort()
        dp = [0] * (max(endTime) + 1)
        arr = [0]
        for job in jobs:
            prev_largest_idx = self.get_prev_idx(job[1], arr)
            curr_max = max(job[2] + dp[prev_largest_idx], dp[arr[-1]])
            dp[job[0]] = max(curr_max, dp[job[0]])
            arr.append(job[0])
        return dp[-1]

    def get_prev_idx(self, target, arr):
        if arr[-1] <= target:
            return arr[-1]
        l, r = 0, len(arr) - 1
        while l < r:
            mid = l + (r - l) // 2
            if arr[mid] > target:
                r = mid
            else:
                l = mid + 1
        return arr[l - 1]
