class Solution:

    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        dcosts = sorted(costs, key=lambda i: i[0] - i[1])
        n = len(costs) // 2
        acost = sum((c[0] for c in dcosts[:n]))
        bcost = sum((c[1] for c in dcosts[n:]))
        return acost + bcost
