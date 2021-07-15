class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        lc = len(costs)
        c = lc//2
        cost1 = 0
        cost2 = 0
        al = c
        bl = c
        for i in range(lc):
            for j in range(i+1, lc):
                if abs(costs[i][0]-costs[i][1]) < abs(costs[j][0]-costs[j][1]):
                    costs[i], costs[j] = costs[j], costs[i]
        
        for i in range(lc):
            if (costs[i][0] <= costs[i][1] and al>0) or bl==0:
                cost1 += costs[i][0]
                al -= 1
            elif bl>0:
                cost1 += costs[i][1]
                bl -= 1
        al = c
        bl = c
        for i in range(lc):
            if (costs[i][0] < costs[i][1] and al>0) or bl == 0:
                cost2 += costs[i][0]
                al -= 1
            elif bl>0:
                cost2 += costs[i][1]
                bl -= 1
        return min(cost1,cost2)

