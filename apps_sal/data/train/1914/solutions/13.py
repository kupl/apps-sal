class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x:x[0]-x[1])
        print(costs)
        firsthalf = costs[0:len(costs)//2]
        secondhalf = costs[len(costs)//2:]
        return sum(f[0] for f in firsthalf) + sum(s[1] for s in secondhalf)

