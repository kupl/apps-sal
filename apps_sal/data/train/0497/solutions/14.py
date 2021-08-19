# from heapq import heappush, heappop
from sortedcontainers import SortedList


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # sort by the starting times
        lst = sorted(zip(startTime, endTime, profit))
        maxprofit, tempstck = 0, SortedList()
        # tempstck -> [(profitval, -endtime)]
        # maxheap -> -maxprofit
        for i in range(len(lst)):
            curr_strt, curr_end, curr_price = lst[i]
            while tempstck and -tempstck[-1][0] <= curr_strt:
                # pop and insert into max heap
                maxprofit = max(tempstck.pop()[1], maxprofit)
            # now do dp
            curr_maxprofit = maxprofit + curr_price
            tempstck.add((-curr_end, curr_maxprofit))
            # don't update maxprofit now because we are not sure whether the next starting price would be greater than current ending price which
            # is why we add it to the temp stack to process it later
        return max(maxprofit, *(i[1] for i in tempstck))
