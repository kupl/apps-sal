class Solution:

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        def binary_search(intervals, index):
            start = 0
            end = index
            while start < end:
                mid = (start + end) // 2
                if intervals[mid][1] > intervals[index][0]:
                    end = mid
                else:
                    start = mid + 1
            return start - 1
        intervals = []
        for i in range(len(startTime)):
            intervals.append((startTime[i], endTime[i], profit[i]))
        intervals.sort(key=lambda i: i[1])
        dp = [0] * len(intervals)
        for i in range(len(intervals)):
            profit_if_i_inlcuded = intervals[i][2]
            k_th = binary_search(intervals, i)
            if k_th != -1:
                profit_if_i_inlcuded += dp[k_th]
            dp[i] = max(dp[i - 1], profit_if_i_inlcuded)
        return max(dp)
