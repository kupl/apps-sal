import bisect


class Solution:
    def jobScheduling(self, start: List[int], end: List[int], profit: List[int]) -> int:
        ans = []
        start_end = []
        dp = []

        for i in range(len(start)):
            start_end.append((start[i], end[i], profit[i]))
            dp.append(-1)
        start_end.sort()
        start.sort()

        def find_next_ind(curr_end):
            return bisect.bisect_left(start, curr_end)

        def recur(ind):
            if ind == len(start_end):
                return 0

            if dp[ind] != -1:
                return dp[ind]

            curr_end = start_end[ind][1]
            curr_profit = start_end[ind][2]

            new_ind = find_next_ind(curr_end)
            ans = max(curr_profit + recur(new_ind), recur(ind + 1))
            dp[ind] = ans
            return ans

        ans = 0
        recur(0)
        for res in dp:
            ans = max(ans, res)
        return ans
