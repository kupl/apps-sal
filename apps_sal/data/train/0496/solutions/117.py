class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        count = collections.Counter(A)
        taken = []
        moves = 0

        for i in range(45000):
            c = count[i]
            if c >= 2:
                taken += (c - 1) * [i]
            elif len(taken) > 0 and c == 0:
                moves += i - taken.pop()

        return moves
