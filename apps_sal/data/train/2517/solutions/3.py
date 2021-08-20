class Solution:

    def tribonacci(self, n: int) -> int:
        T = [0, 1, 1]
        for n in range(3, n + 1):
            T.append(T[n - 3] + T[n - 2] + T[n - 1])
        return T[n]
