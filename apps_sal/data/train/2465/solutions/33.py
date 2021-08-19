class Solution:

    def divisorGame(self, N: int) -> bool:
        res = [False] * (N + 1)
        for i in range(2, N + 1):
            if i % 2 == 0 and res[int(i / 2)] == False:
                res[i] = True
                continue
            for j in range(1, int(math.sqrt(i))):
                if i % j == 0:
                    if res[i - j] == False or (j != 1 and res[i - int(i / j)] == False):
                        res[i] = True
                        break
        return res[N]
