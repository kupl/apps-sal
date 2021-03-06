class Solution:

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit), key=lambda x: (x[1], x[2]))
        N = len(profit)
        dp = [(0, 0, -1)]
        for (idx, (s, e, p)) in enumerate(intervals):
            nonoverlapping_idx = self.find_nonoverlapping_interval(dp, s + 0.1)
            if dp[nonoverlapping_idx][0] + p > dp[idx - 1 + 1][0]:
                dp.append((dp[nonoverlapping_idx][0] + p, e, idx))
            else:
                dp.append(dp[idx - 1 + 1])
        solutions = []
        cur_idx = dp[N][2]
        while cur_idx != -1:
            solutions.insert(0, cur_idx)
            start_idx = intervals[cur_idx][0]
            nonoverlapping_idx = self.find_nonoverlapping_interval(dp, start_idx + 0.1)
            cur_idx = dp[nonoverlapping_idx][2]
        print(solutions)
        return dp[-1][0]

    def find_nonoverlapping_interval(self, dp, start):
        l_idx = 0
        r_idx = len(dp) - 1
        while l_idx <= r_idx:
            mid_idx = (l_idx + r_idx) // 2
            if dp[mid_idx][1] < start:
                l_idx = mid_idx + 1
            else:
                r_idx = mid_idx - 1
        return l_idx - 1
