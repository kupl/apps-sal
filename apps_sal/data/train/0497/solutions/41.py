class Solution:

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        N = len(startTime)
        endtime_ith = sorted([(endTime[i], i) for i in range(N)])
        return self.get_max_profit(max(endTime), {}, endtime_ith, startTime, endTime, profit)

    def get_max_profit(self, end, cache, endtime_ith, startTime, endTime, profit):
        if end in cache:
            return cache[end]
        k = self.floor(endtime_ith, end)
        res = 0
        if k >= 0:
            floor_ith = endtime_ith[k][1]
            boundary = startTime[floor_ith]
            while k >= 0:
                (cur_end_time, original_ith) = endtime_ith[k]
                if cur_end_time < boundary:
                    break
                cur_start_time = startTime[original_ith]
                res = max(res, self.get_max_profit(cur_start_time, cache, endtime_ith, startTime, endTime, profit) + profit[original_ith])
                k -= 1
        cache[end] = res
        return res

    def floor(self, endtime_ith, end):
        res = -1
        (hi, lo) = (len(endtime_ith) - 1, 0)
        while hi >= lo:
            mid = lo + (hi - lo) // 2
            if endtime_ith[mid][0] <= end:
                res = max(res, mid)
                lo = mid + 1
            else:
                hi = mid - 1
        return res
