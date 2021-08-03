from heapq import heappop, heappush, heapify


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        li = []
        A.sort()
        n = len(A)
        if n == 0:
            return 0
        used = {}
        used[A[0]] = 1
        for i in range(1, n):
            if A[i] == A[i - 1]:
                li.append(A[i])
            else:
                used[A[i]] = 1
        res = 0
        t = A[0]
        for x in li:
            while used.get(t, 0) != 0 or t < x:
                t += 1
            used[t] = 1
            res += t - x
        return res
