class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        time_table = list(zip(endTime, startTime, profit))
        time_table.sort()
        cumul_profit = [0 for i in range(len(profit))]
        cumul_profit[0] = time_table[0][2]
        for qu in range(len(time_table)):
            find = 0

            for f in range(qu-1,-1,-1):
                if time_table[f][0] <= time_table[qu][1]:
                    find = cumul_profit[f]
                    break

            cumul_profit[qu] = max(cumul_profit[qu-1], find + time_table[qu][2])
        return cumul_profit[len(profit)-1]

