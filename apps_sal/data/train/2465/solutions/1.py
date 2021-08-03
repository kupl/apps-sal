class Solution:
    def divisorGame(self, N: int) -> bool:
        m = 0
        if N > 1:
            for x in range(1, N):
                N -= x
                m += 1
            if m % 2 == 0:
                return False
            else:
                return True
