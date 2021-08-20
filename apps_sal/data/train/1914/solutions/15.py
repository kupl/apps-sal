class Solution:

    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        sortedCosts = sorted(costs, key=lambda x: abs(x[0] - x[1]), reverse=True)
        numA = 0
        numB = 0
        res = 0
        for cost in sortedCosts:
            if numB >= len(sortedCosts) / 2:
                res += cost[0]
            elif numA >= len(sortedCosts) / 2:
                res += cost[1]
            elif cost[0] < cost[1]:
                res += cost[0]
                numA += 1
            else:
                res += cost[1]
                numB += 1
        return res
