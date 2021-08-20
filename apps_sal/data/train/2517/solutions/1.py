class Solution:

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        F = [0] * 38
        F[0] = 0
        F[1] = 1
        F[2] = 1
        for i in range(3, n + 1):
            F[i] = F[i - 1] + F[i - 2] + F[i - 3]
        return F[n]
