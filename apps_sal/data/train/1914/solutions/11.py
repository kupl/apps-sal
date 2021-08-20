class Solution:

    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diffs = []
        n = len(costs) / 2
        for (i, cost) in enumerate(costs):
            (a, b) = cost
            diff = abs(a - b)
            diffs.append((i, diff))
        diffs = sorted(diffs, key=lambda x: x[1], reverse=True)
        a_count = 0
        b_count = 0
        cost = 0
        print(diffs)
        for (i, diff) in diffs:
            city_a = True
            if costs[i][0] > costs[i][1]:
                if b_count < n:
                    b_count += 1
                    cost += costs[i][1]
                else:
                    a_count += 1
                    cost += costs[i][0]
            elif a_count < n:
                a_count += 1
                cost += costs[i][0]
            else:
                b_count += 1
                cost += costs[i][1]
        return cost
