# sort by difference, where greatest difference is first?
# [[400, 50], [30, 200], [30, 20], [10, 20]]
#   B           A           B         A

# [[840, 118], [259, 770], [448, 54], [926, 667], [577, 469], [184, 139]]
#       B           A           B          B          A            A

# [[631, 42], [343, 819], [457, 60], [650, 359], [451, 713], [536, 709], [855, 779], [515, 563]]
#      B          A           B          B           A           A           B           A

# seemingly works for the given cases

# why??

# positives outweight the negatives
# we will be positive for at least the first n iterations (worst case we pick one city for the first n iterations)

# since we sorted by greatest difference first we will be maximizing our profits by taking
# the optimal choice when the difference is greatest

# we have costs[i] and costs[j] where i <= n and n < j < 2n and difference[i] > difference[j]
# if we make the optimal choice we will be up difference[i] - difference[j]

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

            else:
                if cost[0] < cost[1]:
                    res += cost[0]
                    numA += 1
                else:
                    res += cost[1]
                    numB += 1

        return res
