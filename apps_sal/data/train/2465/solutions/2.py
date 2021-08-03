class Solution:
    memo = {}

    def divisorGame(self, N: int) -> bool:
        return self.move(N)

    def move(self, N):
        if N in self.memo:
            return self.memo[N]
        if N == 2:
            return True
        for f in self.factors(N):
            if self.move(N - f) == False:
                self.memo[N] = True
                return True
        self.memo[N] = False
        return False

    def factors(self, n):
        a = []
        for x in range(1, n):
            if n % x == 0:
                a.append(x)
        return a
