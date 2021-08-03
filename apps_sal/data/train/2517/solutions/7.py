class Solution:
    DP: List[int] = [0, 1, 1]

    def tribonacci(self, n: int) -> int:
        if n >= 0:
            if n < len(self.DP):
                return self.DP[n]
            else:
                offset: int = len(self.DP)
                self.DP.extend([0] * (n - offset + 1))
                for i in range(offset, n + 1):
                    self.DP[i] = self.DP[i - 3] + self.DP[i - 2] + self.DP[i - 1]
                return self.DP[n]
        else:
            raise ValueError
