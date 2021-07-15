from bisect import bisect_left

class Solution:
    def jobScheduling(self, start_times: List[int], end_times: List[int], profits: List[int]) -> int:
        start_times, end_times, profits = list(zip(*sorted(zip(start_times, end_times, profits))))
        n = len(start_times)
        cache = {n - 1 : profits[n - 1], n : 0}
        
        def max_profit(i):
            if i not in cache:
                next_start = bisect_left(start_times, end_times[i])
                cache[i] = max(profits[i] + max_profit(next_start), max_profit(i + 1))
            return cache[i]
        
        return max_profit(0)

