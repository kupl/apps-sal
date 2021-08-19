class Solution:

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        comb = []
        dd = dict()
        for i in range(len(startTime)):
            comb.append((startTime[i], endTime[i], profit[i]))
        comb.sort()
        print(comb)
        l = len(comb)

        def returnIdx(idx, l, val):
            while idx < l:
                mid = idx + (l - idx) // 2
                if comb[mid][0] < val:
                    idx = mid + 1
                else:
                    l = mid
            return idx

        def maxProfit(jobidx):
            if jobidx == l:
                return 0
            if jobidx in dd:
                return dd[jobidx]
            ans = 0
            ans = max(ans, maxProfit(jobidx + 1))
            ans = max(ans, comb[jobidx][2] + maxProfit(returnIdx(jobidx, l, comb[jobidx][1])))
            dd[jobidx] = ans
            return ans
        return maxProfit(0)
