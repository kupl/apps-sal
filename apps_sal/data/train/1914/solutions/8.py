class Solution:

    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        c = []
        asum = 0
        for i in range(len(costs)):
            (a, b) = costs[i]
            price = b - a
            asum += a
            c.append(price)
        refunds = sorted(c)
        for i in range(len(refunds) // 2):
            asum += refunds[i]
        return asum
