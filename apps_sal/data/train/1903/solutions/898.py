# alright, whatever, time to solve it again in Python3 \\U0001f40d  whoo!

# ok silly mistake, but that's A ok :)

class Solution:
    def minCostConnectPoints(self, A: List[List[int]]) -> int:
        N = len(A)
        P = [i for i in range(N)]  # parent representatives of disjoint sets
        E = []
        for i in range(N):
            x1, y1 = A[i]
            for j in range(i + 1, N):
                x2, y2 = A[j]
                E.append([abs(x1 - x2) + abs(y1 - y2), i, j])
        E.sort()

        def find(x):
            P[x] = P[x] if P[x] == x else find(P[x])
            return P[x]

        def union(a, b):
            a = find(a)
            b = find(b)
            if a == b:
                return False
            P[a] = b   # arbitrary choice
            return True
        return sum([cost for cost, u, v in E if union(u, v)])
        # for cost, u, v in E:
        #     if union(u, v):
        #         total += cost
        # return total
