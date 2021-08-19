class Solution:

    def divisorGame(self, N: int) -> bool:
        game = [False for i in range(N + 1)]
        for i in range(2, N + 1):
            for j in range(1, i):
                if i % j == 0 and game[i - j] == False:
                    game[i] = True
                    break
        return game[N]
