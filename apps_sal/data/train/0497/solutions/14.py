from sortedcontainers import SortedList


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        lst = sorted(zip(startTime, endTime, profit))
        maxprofit, tempstck = 0, SortedList()
        for i in range(len(lst)):
            curr_strt, curr_end, curr_price = lst[i]
            while tempstck and -tempstck[-1][0] <= curr_strt:
                maxprofit = max(tempstck.pop()[1], maxprofit)
            curr_maxprofit = maxprofit + curr_price
            tempstck.add((-curr_end, curr_maxprofit))
        return max(maxprofit, *(i[1] for i in tempstck))
