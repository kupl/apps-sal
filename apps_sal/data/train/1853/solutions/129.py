import numpy as np


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        A = np.zeros([n, n])
        for e in edges:
            A[e[0]][e[1]] = e[2]
            A[e[1]][e[0]] = e[2]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if A[i][j] == 0:
                    A[i][j] = np.inf
        for k in range(n):
            for i in range(n):
                if (i == k):
                    continue
                for j in range(n):
                    if (j == k):
                        continue
                    A[i, j] = min(A[i, j], A[i, k] + A[k, j])
        # print(A)
        count = np.sum(A <= distanceThreshold, axis=0)
        minn = count[0]
        # print(count)
        argminn = 0
        for i, c in enumerate(count):
            if c <= minn:
                minn = c
                argminn = i
        return argminn
