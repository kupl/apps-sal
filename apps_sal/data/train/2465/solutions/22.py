from collections import defaultdict as dd


class Solution:
    def __init__(self):
        self.d = dd()

    def divisorGame(self, n: int) -> bool:
        return self.__will_win(n)

    def __will_win(self, n: int):

        for i in range(1, n):
            if n % i != 0:
                continue

            if n - i in self.d:
                wins = self.d[n - i]
            else:
                wins = self.__will_win(n - i)
                self.d[n - i] = wins

            if not wins:
                return True

        return False
