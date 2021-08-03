class Solution:
    def divisorGame(self, N: int) -> bool:
        memo = set()

        def check(factor, player):
            if factor == 1:
                return player != 'A'
            if factor in memo:
                return False
            player = 'A' if player == 'B' else 'B'

            for i in range(1, 1 + (factor // 2)):
                if factor % i == 0:
                    memo.add(factor)
                    if check(factor - i, player):
                        return True
        return check(N, 'A')
