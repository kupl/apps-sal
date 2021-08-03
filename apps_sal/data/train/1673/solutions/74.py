class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        costs = [[None for i in range(len(A))] for j in range(len(A[0]))]

        for j in range(len(A)):
            costs[0] = A[0]

        for i in range(1, len(A)):
            for j in range(len(A)):
                parents = list()
                for p in range(len(A)):
                    if p != j:
                        parents.append(costs[i - 1][p])

                costs[i][j] = min(parents) + A[i][j]

        return min(costs[len(A) - 1])
